from core.interfaces.repositories import UserRepository, SessionRepository
from core.interfaces.output_ports import OutputPort
from core.use_cases.dtos import StartCounselingInputDTO, StartCounselingOutputDTO
from core.entities.session import Session
import uuid

class StartCounselingUseCase:
    """P1 -> P2 진입 시 웰컴 메시지 및 세션 초기화 로직"""
    def __init__(
        self,
        user_repo: UserRepository,
        session_repo: SessionRepository,
        output_port: OutputPort[StartCounselingOutputDTO]
    ):
        self.user_repo = user_repo
        self.session_repo = session_repo
        self.output_port = output_port

    def execute(self, request: StartCounselingInputDTO) -> None:
        user = self.user_repo.get_by_id(request.user_id)
        if not user:
            self.output_port.failure("User not found")
            return

        # 세션 초기화
        session_id = str(uuid.uuid4())
        new_session = Session(session_id=session_id, user_id=user.user_id)
        self.session_repo.save(new_session)

        # 웰컴 메시지 생성 (Ice Breaking)
        welcome_msg = f"안녕하세요, {user.nickname}님! 오늘 들려주실 이야기가 있나요?"
        
        response = StartCounselingOutputDTO(
            session_id=session_id,
            welcome_message=welcome_msg
        )
        self.output_port.success(response)
