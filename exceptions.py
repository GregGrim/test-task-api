from starlette.requests import Request
from starlette.responses import JSONResponse


class AppException(Exception):
    def __init__(self, status_code: int, detail: str, headers: dict = None):
        super().__init__()
        self.status_code = status_code
        self.detail = detail
        self.headers = headers or {}


class ProductDoesNotExistException(AppException):
    def __init__(self):
        super().__init__(status_code=404, detail="Product does not exist")


async def app_exception_handler(request: Request, exc: AppException) -> JSONResponse:
    return JSONResponse(
        status_code=exc.status_code, content={"detail": exc.detail}, headers=exc.headers
    )
