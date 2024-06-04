from sqlalchemy.orm import Session

from entities.product import CreateProduct, Product, EditProduct
from exceptions import ProductDoesNotExistException
from models.product_models import ProductModel, Base


class ProductRepository:

    def __init__(self, engine):
        self.engine = engine

    # better to use alembic db migration but to simplify we can do this
    def create_tables(self):
        Base.metadata.create_all(self.engine)

    def get_products(self, page: int, limit: int, category: str | None) -> list[Product]:
        with Session(self.engine) as session:
            query = session.query(ProductModel)
            if category:
                query = query.filter(ProductModel.category == category)

            products = query.offset((page - 1) * limit).limit(limit).all()
        return [Product.model_validate(product) for product in products]

    def add_product(self, product: CreateProduct) -> Product:
        with Session(self.engine) as session:
            product = product.model_dump()
            new_product = ProductModel(**product)

            session.add(new_product)
            session.commit()

            session.refresh(new_product)

        return Product.model_validate(new_product)

    def edit_product(self, product_id: str, product_data: EditProduct) -> Product:
        with Session(self.engine) as session:
            product = self._get_product_by_id(product_id)

            update_data = product_data.model_dump(exclude_none=True)

            for key, value in update_data.items():
                setattr(product, key, value)

            session.add(product)
            session.commit()
            session.refresh(product)
        return Product.model_validate(product)

    def _get_product_by_id(self, product_id: str) -> ProductModel:
        with Session(self.engine) as session:
            product = session.query(ProductModel).where(ProductModel.id == product_id).first()
            if not product:
                raise ProductDoesNotExistException()
        return product

    def delete_product(self, product_id: str):
        with Session(self.engine) as session:
            product = self._get_product_by_id(product_id)
            session.delete(product)
            session.commit()
