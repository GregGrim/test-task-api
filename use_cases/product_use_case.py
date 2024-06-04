from entities.pagination import Paginated
from entities.product import EditProduct
from repositories.product_repository import ProductRepository


class ProductUseCase:
    def __init__(self, product_repo: ProductRepository):
        self.product_repo = product_repo

    def get_products(self, page, limit):
        products = self.product_repo.get_products(page=page, limit=limit)
        return Paginated(items=products, count=len(products))

    def add_product(self, product):
        return self.product_repo.add_product(product)

    def edit_product(self, id: str, product: EditProduct):
        return self.product_repo.edit_product(product_id=id, product_data=product)

    def delete_product(self, product_id):
        return self.product_repo.delete_product(product_id)
