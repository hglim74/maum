from dataclasses import dataclass
from typing import Optional

@dataclass
class User:
    """사용자 엔티티 (ID, 닉네임, 동의 상태 등)"""
    user_id: str
    nickname: str
    is_consent_given: bool = False
    persona_summary: Optional[str] = None
