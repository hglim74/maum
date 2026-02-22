from typing import Any, Dict, Optional
from core.interfaces.output_ports import OutputPort

class HTTPPresenter(OutputPort):
    def __init__(self):
        self.data: Dict[str, Any] = {}
        self.error: Optional[str] = None
        self.status_code: int = 200

    def success(self, response: Any) -> None:
        self.data = response
        self.status_code = 200

    def failure(self, message: str) -> None:
        self.error = message
        self.status_code = 400
        self.data = {"error": message}
