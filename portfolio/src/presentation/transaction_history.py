from typing import List

from fastapi import APIRouter, Depends

from src.domain.transaction_history.schema import TransactionHistorySchema
from src.service.transaction_history_service import TransactionHistoryService


class TransactionHistoryRouter:
    api_router = APIRouter(prefix="/transaction_history", tags=["Transaction History"])

    @staticmethod
    @api_router.get(
        "",
        response_model=List[TransactionHistorySchema],
    )
    async def get_transactions_history(
        parameter: str = "created_at",
        transactions: TransactionHistoryService = Depends(TransactionHistoryService),
    ):
        return await transactions.get_transactions_history_list(parameter=parameter)
