from typing import List

from fastapi import APIRouter, Depends

from src.domain.history.schema import TransactionHistorySchema
from src.service.service import TransactionHistoryService


class TransactionHistoryRouter:
    api_router = APIRouter(prefix="/history", tags=["Transaction History"])

    @staticmethod
    @api_router.get("", response_model=List[TransactionHistorySchema])
    async def get_transactions_history(
        parameter: str = "created_at",
        account: TransactionHistoryService = Depends(TransactionHistoryService),
    ):
        return await account.get_transactions_history_list(parameter=parameter)
