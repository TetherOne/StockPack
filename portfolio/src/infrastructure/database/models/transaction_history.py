from sqlalchemy.orm import Mapped

from src.infrastructure.database.models.base import Base
from src.infrastructure.database.models.mixins.create_time import CreateTimeMixin
from src.infrastructure.database.models.mixins.id_int_pk import IdIntPkMixin


class TransactionHistory(
    Base,
    IdIntPkMixin,
    CreateTimeMixin,
):
    ticker: Mapped[str]
    price: Mapped[str]
