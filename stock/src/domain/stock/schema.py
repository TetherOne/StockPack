from pydantic import BaseModel


class StockTickerBaseSchema(BaseModel):
    ticker: str


class StockTickerSchema(StockTickerBaseSchema):
    price: float
