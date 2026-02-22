from core.interfaces.repositories import SessionRepository, MessageRepository, ReportRepository
from core.interfaces.ai_gateways import AIGateway
from core.interfaces.output_ports import OutputPort
from core.use_cases.dtos import FinishCounselingInputDTO, FinishCounselingOutputDTO
from core.entities.report import Report
from datetime import datetime
import uuid

class FinishCounselingUseCase:
    """P2 -> P3 상담 종료 및 리포트 생성 로직"""
    def __init__(
        self,
        session_repo: SessionRepository,
        message_repo: MessageRepository,
        report_repo: ReportRepository,
        ai_gateway: AIGateway,
        output_port: OutputPort[FinishCounselingOutputDTO]
    ):
        self.session_repo = session_repo
        self.message_repo = message_repo
        self.report_repo = report_repo
        self.ai_gateway = ai_gateway
        self.output_port = output_port

    def execute(self, request: FinishCounselingInputDTO) -> None:
        session = self.session_repo.get_by_id(request.session_id)
        if not session:
            self.output_port.failure("Session not found")
            return

        # 세션 종료 상태 업데이트
        session.status.value = "finished" 
        session.end_time = datetime.now()
        self.session_repo.save(session)

        # 대화 내용 요약 및 감정 흐름 분석 (AI 활용)
        messages = self.message_repo.get_by_session_id(request.session_id)
        msg_text = "\n".join([f"{m.sender}: {m.text}" for m in messages])
        summary = self.ai_gateway.summarize_session(msg_text)
        
        # 리포트 생성
        report_id = str(uuid.uuid4())
        report = Report(
            report_id=report_id,
            session_id=request.session_id,
            summary=summary,
            emotion_flow=[{"time": i, "value": 0.5} for i in range(len(messages))]
        )
        self.report_repo.save(report)

        response = FinishCounselingOutputDTO(
            report_id=report_id,
            summary=summary,
            emotion_flow=report.emotion_flow
        )
        self.output_port.success(response)
