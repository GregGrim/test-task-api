import sqlalchemy as sa
from fastapi import Query, Security
from fastapi.security import APIKeyHeader
from starlette.exceptions import HTTPException
from starlette.status import HTTP_403_FORBIDDEN

from settings import app_settings
from entities.pagination import Pagination
from repositories.product_repository import ProductRepository
from use_cases.product_use_case import ProductUseCase

api_key_header = APIKeyHeader(name=app_settings.API_KEY, auto_error=False)


def get_product_use_case() -> ProductUseCase:
    product_repo = ProductRepository(
        engine=sa.create_engine(
            app_settings.DATABASE_URL
        )
    )
    product_repo.create_tables()
    return ProductUseCase(product_repo)


def get_pagination(
        page: int = Query(1, ge=1),
        limit: int = Query(100, ge=0),
) -> Pagination:
    return Pagination(page=page, limit=limit)


def get_api_key(api_key_header: str = Security(api_key_header)):
    if api_key_header == app_settings.API_KEY:
        return api_key_header
    else:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Could not validate credentials"
        )
