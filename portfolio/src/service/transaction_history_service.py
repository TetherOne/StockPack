from typing import Optional, List

from fastapi import Depends

from src.application.container import Container
from src.domain.transaction_history.repository import TransactionHistoryReadRepository
from src.domain.transaction_history.schema import TransactionHistorySchema


class TransactionHistoryService:
    def __init__(
        self,
        read_repository: TransactionHistoryReadRepository = Depends(
            Container.transaction_history_read_repository
        ),
    ):
        self.read_repo = read_repository

    async def get_transactions_history_list(
        self,
        parameter: str,
    ) -> Optional[List[TransactionHistorySchema]]:
        return await self.read_repo.get_list(parameter=parameter)
