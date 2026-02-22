from typing import Optional, List, Dict
from core.interfaces.repositories import UserRepository, SessionRepository, MessageRepository, ReportRepository
from core.entities.user import User
from core.entities.session import Session, SessionStatus
from core.entities.message import Message
from core.entities.report import Report

class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self._users: Dict[str, User] = {}

    def get_by_id(self, user_id: str) -> Optional[User]:
        return self._users.get(user_id)

    def save(self, user: User) -> None:
        self._users[user.user_id] = user

class InMemorySessionRepository(SessionRepository):
    def __init__(self):
        self._sessions: Dict[str, Session] = {}

    def get_by_id(self, session_id: str) -> Optional[Session]:
        return self._sessions.get(session_id)

    def get_active_session_by_user_id(self, user_id: str) -> Optional[Session]:
        for session in self._sessions.values():
            if session.user_id == user_id and session.status == SessionStatus.ACTIVE:
                return session
        return None

    def save(self, session: Session) -> None:
        self._sessions[session.session_id] = session

class InMemoryMessageRepository(MessageRepository):
    def __init__(self):
        self._messages: List[Message] = []

    def save(self, message: Message) -> None:
        self._messages.append(message)

    def get_by_session_id(self, session_id: str) -> List[Message]:
        return [m for m in self._messages if m.session_id == session_id]

class InMemoryReportRepository(ReportRepository):
    def __init__(self):
        self._reports: Dict[str, Report] = {}

    def save(self, report: Report) -> None:
        self._reports[report.session_id] = report

    def get_by_session_id(self, session_id: str) -> Optional[Report]:
        return self._reports.get(session_id)
