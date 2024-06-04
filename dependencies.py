import sqlalchemy as sa
from fastapi import Query

from entities.pagination import Pagination
from repositories.product_repository import ProductRepository
from use_cases.product_use_case import ProductUseCase


def get_product_use_case() -> ProductUseCase:
    product_repo = ProductRepository(
        engine=sa.create_engine(
            "sqlite:///./product_database.db"
        )
    )
    product_repo.create_tables()
    return ProductUseCase(product_repo)


def get_pagination(
        page: int = Query(1, ge=1),
        limit: int = Query(100, ge=0),
) -> Pagination:
    return Pagination(page=page, limit=limit)
