from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, Any

@dataclass
class Message:
    """대화 메시지 엔티티 (발화자, 텍스트, 감정 메타데이터)"""
    message_id: str
    session_id: str
    sender: str  # 'user' or 'ai'
    text: str
    timestamp: datetime = field(default_factory=datetime.now)
    emotion_metadata: Dict[str, Any] = field(default_factory=dict)
