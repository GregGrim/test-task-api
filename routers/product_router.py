from typing import Annotated

from fastapi import Depends, APIRouter
from starlette import status
from starlette.responses import Response

from dependencies import get_product_use_case, get_pagination
from entities.pagination import Paginated, Pagination
from entities.product import Product, CreateProduct, EditProduct
from exceptions import ProductDoesNotExistException
from use_cases.product_use_case import ProductUseCase

router = APIRouter(prefix="/products", tags=["products"])


@router.get("/get-products", response_model=Paginated[Product], status_code=status.HTTP_200_OK)
async def get_products(
        product_use_case: Annotated[ProductUseCase, Depends(get_product_use_case)],
        pagination: Annotated[Pagination, Depends(get_pagination)],
):
    return product_use_case.get_products(pagination.page, pagination.limit)


@router.put("/add-product", response_model=Product, status_code=status.HTTP_201_CREATED)
async def add_product(
        product: CreateProduct, product_use_case: Annotated[ProductUseCase, Depends(get_product_use_case)]
):
    return product_use_case.add_product(product)


@router.patch("/edit-product/{product_id}", response_model=Product, status_code=status.HTTP_200_OK)
async def edit_product(
        product_id: str,
        product: EditProduct,
        product_use_case: Annotated[ProductUseCase, Depends(get_product_use_case)],
):
    try:
        result = product_use_case.edit_product(id=product_id, product=product)
    except ProductDoesNotExistException:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    return result


@router.delete("/delete-product/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(
        product_id: str,
        product_use_case: Annotated[ProductUseCase, Depends(get_product_use_case)],
):
    try:
        product_use_case.delete_product(product_id)
    except ProductDoesNotExistException:
        return

    return Response(status_code=status.HTTP_204_NO_CONTENT)
