from entities.pagination import Paginated
from entities.product import EditProduct, Product, CreateProduct
from repositories.product_repository import ProductRepository


class ProductUseCase:
    def __init__(self, product_repo: ProductRepository):
        self.product_repo = product_repo

    def get_products(self, page: int, limit: int, category: str | None) -> Paginated:
        products = self.product_repo.get_products(page, limit, category)
        return Paginated(items=products, count=len(products))

    def add_product(self, product: CreateProduct) -> Product:
        return self.product_repo.add_product(product)

    def edit_product(self, product_id: str, product: EditProduct) -> Product:
        return self.product_repo.edit_product(product_id, product_data=product)

    def delete_product(self, product_id: str):
        return self.product_repo.delete_product(product_id)
