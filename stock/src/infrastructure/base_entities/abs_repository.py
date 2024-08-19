from abc import ABC, abstractmethod
from typing import Generic, Any

from src.infrastructure.base_entities import table_type


class AbstractReadRepository(ABC, Generic[table_type]):
    def __init__(self):
        self.model = table_type

    @abstractmethod
    async def get(self, **kwargs) -> Any:
        raise NotImplementedError
