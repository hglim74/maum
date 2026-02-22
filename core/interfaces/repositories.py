from abc import ABC, abstractmethod
from typing import Optional, List
from core.entities.user import User
from core.entities.session import Session
from core.entities.message import Message
from core.entities.report import Report

class UserRepository(ABC):
    @abstractmethod
    def get_by_id(self, user_id: str) -> Optional[User]:
        pass

    @abstractmethod
    def save(self, user: User) -> None:
        pass

class SessionRepository(ABC):
    @abstractmethod
    def get_by_id(self, session_id: str) -> Optional[Session]:
        pass

    @abstractmethod
    def get_active_session_by_user_id(self, user_id: str) -> Optional[Session]:
        pass

    @abstractmethod
    def save(self, session: Session) -> None:
        pass

class MessageRepository(ABC):
    @abstractmethod
    def save(self, message: Message) -> None:
        pass

    @abstractmethod
    def get_by_session_id(self, session_id: str) -> List[Message]:
        pass

class ReportRepository(ABC):
    @abstractmethod
    def save(self, report: Report) -> None:
        pass

    @abstractmethod
    def get_by_session_id(self, session_id: str) -> Optional[Report]:
        pass
