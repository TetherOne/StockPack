from typing import Optional, List, Any

from sqlalchemy import select
from sqlalchemy.ext.asyncio import async_sessionmaker

from src.domain.transaction_history.schema import TransactionHistorySchema
from src.infrastructure.base_entities.abs_repository import AbstractReadRepository
from src.infrastructure.database.db_helper import DatabaseHelper
from src.infrastructure.database.models import TransactionHistory


class TransactionHistoryReadRepository(AbstractReadRepository):
    def __init__(self, db_helper: DatabaseHelper):
        super().__init__()
        self.model = TransactionHistory
        self.transactional_session: async_sessionmaker = db_helper.session_factory
        self.async_session_factory: async_sessionmaker = db_helper.session_factory

    async def get_list(
        self,
        parameter: Any = "created_at",
    ) -> Optional[List[TransactionHistorySchema]]:
        async with self.transactional_session() as session:
            final = None
            if option := getattr(self.model, parameter):
                stmt = select(self.model).order_by(option)
                result = await session.execute(stmt)
                final = result.scalars().all()
        return final
