import datetime as dt

from pydantic import BaseModel, ConfigDict, Field


class BaseProduct(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name: str
    description: str
    price: float
    stock: int = Field(ge=0)


class Product(BaseProduct):
    id: str
    date_created: dt.datetime
    category: str | None


class CreateProduct(BaseProduct):
    pass


class EditProduct(BaseModel):
    name: str | None = None
    description: str | None = None
    price: float | None = None
    stock: int | None = None
    category: str | None = None
