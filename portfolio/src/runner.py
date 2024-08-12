from fastapi import FastAPI

from .application.server import ApiServer

app_portfolio = ApiServer(FastAPI()).get_app()
