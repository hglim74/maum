from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar('T')

class OutputPort(ABC, Generic[T]):
    @abstractmethod
    def success(self, response: T) -> None:
        pass

    @abstractmethod
    def failure(self, message: str) -> None:
        pass
