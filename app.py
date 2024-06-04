import fastapi
from fastapi import FastAPI

from routers import product_router
from exceptions import AppException, app_exception_handler


def _add_exc_handlers(app: FastAPI):
    app.add_exception_handler(AppException, app_exception_handler)


def _add_routers(app: FastAPI):
    app.include_router(product_router.router)


def create_app() -> FastAPI:
    app = fastapi.FastAPI()
    _add_exc_handlers(app)
    _add_routers(app)
    return app
