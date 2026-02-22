import os
from core.interfaces.ai_gateways import AIGateway

class GeminiAIGateway(AIGateway):
    def __init__(self, api_key: str):
        self.api_key = api_key
        # In a real implementation, we would initialize the Gemini client here.
        # for now, we'll provide mock logic that simulates AI behavior.

    def analyze_emotion(self, text: str) -> str:
        # Mock sentiment analysis
        if "슬퍼" in text or "우울" in text:
            return "sadness"
        elif "기뻐" in text or "행복" in text:
            return "joy"
        return "neutral"

    def generate_empathic_response(self, text: str, context: str) -> str:
        # Mock LLM generation
        emotion = self.analyze_emotion(text)
        if emotion == "sadness":
            return "정말 많이 힘드셨겠어요. 제가 당신의 마음을 조금이나마 위로해 드리고 싶어요."
        return f"말씀해 주셔서 감사해요. '{text}'에 대해 더 자세히 이야기해 보실까요?"

    def summarize_session(self, messages: str) -> str:
        # Mock summarization
        return "전반적인 대화 요약: 사용자는 자신의 감정을 솔직하게 표현했으며, 정서적 지지를 받았습니다."
