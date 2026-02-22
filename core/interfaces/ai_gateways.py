from abc import ABC, abstractmethod
from typing import Dict, Any

class AIGateway(ABC):
    @abstractmethod
    def analyze_emotion(self, text: str) -> str:
        pass

    @abstractmethod
    def generate_empathic_response(self, text: str, context: str) -> str:
        pass

    @abstractmethod
    def summarize_session(self, messages: str) -> str:
        pass
