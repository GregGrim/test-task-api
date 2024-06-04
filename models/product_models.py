import datetime as dt
import uuid

import sqlalchemy as sa

from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class ProductModel(Base):
    __tablename__ = "products"

    id = sa.Column(
        sa.String, primary_key=True, default=lambda: str(uuid.uuid4())
    )
    name = sa.Column(String, index=True)
    description = sa.Column(String, index=True)
    price = sa.Column(Float, index=True)
    stock = sa.Column(Integer, index=True)
    date_created = sa.Column(sa.DateTime, default=dt.datetime.utcnow())
    category = sa.Column(String, index=True, default=None)
