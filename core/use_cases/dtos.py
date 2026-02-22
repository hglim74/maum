from dataclasses import dataclass
from typing import List, Optional, Dict, Any
from datetime import datetime

# Start Counseling
@dataclass
class StartCounselingInputDTO:
    user_id: str

@dataclass
class StartCounselingOutputDTO:
    session_id: str
    welcome_message: str

# Chat Counseling
@dataclass
class ChatCounselingInputDTO:
    session_id: str
    user_id: str
    text: str

@dataclass
class ChatCounselingOutputDTO:
    ai_response: str
    detected_emotion: str

# Finish Counseling
@dataclass
class FinishCounselingInputDTO:
    session_id: str

@dataclass
class FinishCounselingOutputDTO:
    report_id: str
    summary: str
    emotion_flow: List[Dict[str, float]]

# Manage History
@dataclass
class ManageHistoryInputDTO:
    user_id: str

@dataclass
class HistoryItemDTO:
    session_id: str
    start_time: datetime
    summary: str

@dataclass
class ManageHistoryOutputDTO:
    history: List[HistoryItemDTO]
