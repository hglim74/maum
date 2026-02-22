from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Dict

@dataclass
class Report:
    """마음 리포트 엔티티 (감정 변화 지표, 요약 텍스트)"""
    report_id: str
    session_id: str
    summary: str
    emotion_flow: List[Dict[str, float]] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.now)
