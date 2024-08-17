from typing import TypeVar

from fastapi import FastAPI

from src.presentation.transaction_history import TransactionHistoryRouter

FastAPIInstance = TypeVar("FastAPIInstance", bound=FastAPI)


class ApiServer:
    def __init__(self, app: FastAPI):
        self.__app = app
        self.__app.include_router(TransactionHistoryRouter().api_router)

    def get_app(self) -> FastAPIInstance:
        return self.__app


app_portfolio = ApiServer(FastAPI()).get_app()
