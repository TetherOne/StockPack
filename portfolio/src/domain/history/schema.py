from datetime import datetime

from pydantic import BaseModel


class TransactionHistoryBaseSchema(BaseModel):
    ticker: str
    price: float


class TransactionHistorySchema(TransactionHistoryBaseSchema):
    id: int
    created_at: datetime


class TransactionHistoryCreateSchema(TransactionHistoryBaseSchema):
    pass
