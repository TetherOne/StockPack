from src.domain.transaction_history.repository import TransactionHistoryReadRepository
from src.infrastructure.base_entities.singleton import Singleton, OnlyContainer
from src.infrastructure.database.db_helper import db_helper


class Container(Singleton):
    transaction_history_read_repository = OnlyContainer(
        TransactionHistoryReadRepository,
        db_helper,
    )
