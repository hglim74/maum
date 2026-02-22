from core.interfaces.repositories import MessageRepository, SessionRepository
from core.interfaces.ai_gateways import AIGateway
from core.interfaces.output_ports import OutputPort
from core.use_cases.dtos import ChatCounselingInputDTO, ChatCounselingOutputDTO
from core.entities.message import Message
import uuid

class ChatCounselingUseCase:
    """P2 메시지 송수신, 감정 분석, 공감 응답 생성 파이프라인"""
    def __init__(
        self,
        session_repo: SessionRepository,
        message_repo: MessageRepository,
        ai_gateway: AIGateway,
        output_port: OutputPort[ChatCounselingOutputDTO]
    ):
        self.session_repo = session_repo
        self.message_repo = message_repo
        self.ai_gateway = ai_gateway
        self.output_port = output_port

    def execute(self, request: ChatCounselingInputDTO) -> None:
        session = self.session_repo.get_by_id(request.session_id)
        if not session or session.status.value != "active":
            self.output_port.failure("Active session not found")
            return

        # 사용자 메시지 저장
        user_msg = Message(
            message_id=str(uuid.uuid4()),
            session_id=request.session_id,
            sender="user",
            text=request.text
        )
        self.message_repo.save(user_msg)

        # AI 호출 및 감정 분석 수행 (DIP 준수)
        detected_emotion = self.ai_gateway.analyze_emotion(request.text)
        
        # 이전 대화 맥락이 필요할 경우 repository에서 가져올 수 있음
        context = "" # Skip for skeleton simplification
        ai_response_text = self.ai_gateway.generate_empathic_response(request.text, context)

        # AI 메시지 저장
        ai_msg = Message(
            message_id=str(uuid.uuid4()),
            session_id=request.session_id,
            sender="ai",
            text=ai_response_text,
            emotion_metadata={"detected": detected_emotion}
        )
        self.message_repo.save(ai_msg)

        response = ChatCounselingOutputDTO(
            ai_response=ai_response_text,
            detected_emotion=detected_emotion
        )
        self.output_port.success(response)
