from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Optional

class SessionStatus(Enum):
    ACTIVE = "active"
    FINISHED = "finished"

@dataclass
class Session:
    """상담 세션 엔티티 (상태, 시작/종료 시간)"""
    session_id: str
    user_id: str
    status: SessionStatus = SessionStatus.ACTIVE
    start_time: datetime = field(default_factory=datetime.now)
    end_time: Optional[datetime] = None
