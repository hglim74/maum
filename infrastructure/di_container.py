from infrastructure.adapters.repositories.in_memory_repos import (
    InMemoryUserRepository,
    InMemorySessionRepository,
    InMemoryMessageRepository,
    InMemoryReportRepository
)
from infrastructure.adapters.gateways.gemini_client import GeminiAIGateway
from core.use_cases.start_counseling import StartCounselingUseCase
from core.use_cases.chat_counseling import ChatCounselingUseCase
from core.use_cases.finish_counseling import FinishCounselingUseCase
from core.use_cases.manage_history import ManageHistoryUseCase
from core.entities.user import User

class DIContainer:
    def __init__(self):
        # Repositories (Persist across requests in this mock)
        self.user_repo = InMemoryUserRepository()
        self.session_repo = InMemorySessionRepository()
        self.message_repo = InMemoryMessageRepository()
        self.report_repo = InMemoryReportRepository()
        
        # Gateways
        self.ai_gateway = GeminiAIGateway(api_key="mock-key")
        
        # Seed a mock user
        self.user_repo.save(User(user_id="user123", nickname="마음이", is_consent_given=True))

    def get_start_counseling_use_case(self, presenter):
        return StartCounselingUseCase(self.user_repo, self.session_repo, presenter)

    def get_chat_counseling_use_case(self, presenter):
        return ChatCounselingUseCase(self.session_repo, self.message_repo, self.ai_gateway, presenter)

    def get_finish_counseling_use_case(self, presenter):
        return FinishCounselingUseCase(self.session_repo, self.message_repo, self.report_repo, self.ai_gateway, presenter)

    def get_manage_history_use_case(self, presenter):
        return ManageHistoryUseCase(self.user_repo, self.session_repo, self.report_repo, presenter)
