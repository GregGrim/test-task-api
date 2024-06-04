from typing import TypeVar, Generic

from pydantic import BaseModel

T = TypeVar("T")


class Paginated(BaseModel, Generic[T]):
    items: list[T]
    count: int


class Pagination(BaseModel):
    page: int
    limit: int
