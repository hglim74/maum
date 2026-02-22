from core.interfaces.repositories import SessionRepository, ReportRepository, UserRepository
from core.interfaces.output_ports import OutputPort
from core.use_cases.dtos import ManageHistoryInputDTO, ManageHistoryOutputDTO, HistoryItemDTO

class ManageHistoryUseCase:
    """P4 히스토리 조회 및 페르소나 업데이트 로직"""
    def __init__(
        self,
        user_repo: UserRepository,
        session_repo: SessionRepository,
        report_repo: ReportRepository,
        output_port: OutputPort[ManageHistoryOutputDTO]
    ):
        self.user_repo = user_repo
        self.session_repo = session_repo
        self.report_repo = report_repo
        self.output_port = output_port

    def execute(self, request: ManageHistoryInputDTO) -> None:
        # Mock logic: Get sessions and their reports
        # In real impl, would fetch from repo
        history_items = [
            HistoryItemDTO(
                session_id="mock-session-1",
                start_time=None, # Should be datetime
                summary="지난 상담 요약 내용"
            )
        ]

        response = ManageHistoryOutputDTO(history=history_items)
        self.output_port.success(response)

    def update_user_persona(self, user_id: str, insights: str) -> None:
        user = self.user_repo.get_by_id(user_id)
        if user:
            user.persona_summary = insights
            self.user_repo.save(user)
