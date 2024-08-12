from fastapi import FastAPI

from .application.server import ApiServer

app_stock = ApiServer(FastAPI()).get_app()
