from fastapi import FastAPI, Body
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from infrastructure.di_container import DIContainer
from infrastructure.adapters.controllers.http_presenters import HTTPPresenter
from core.use_cases.dtos import (
    StartCounselingInputDTO,
    ChatCounselingInputDTO,
    FinishCounselingInputDTO,
    ManageHistoryInputDTO
)
import os

app = FastAPI(title="Mind Connect API")
container = DIContainer()

# Get static files path
static_dir = os.path.join(os.path.dirname(__file__), "static")

# Endpoints
@app.post("/counseling/start")
def start_counseling(user_id: str = Body(..., embed=True)):
    presenter = HTTPPresenter()
    use_case = container.get_start_counseling_use_case(presenter)
    use_case.execute(StartCounselingInputDTO(user_id=user_id))
    return presenter.data

@app.post("/counseling/chat")
def chat_counseling(session_id: str = Body(...), user_id: str = Body(...), text: str = Body(...)):
    presenter = HTTPPresenter()
    use_case = container.get_chat_counseling_use_case(presenter)
    use_case.execute(ChatCounselingInputDTO(session_id=session_id, user_id=user_id, text=text))
    return presenter.data

@app.post("/counseling/finish")
def finish_counseling(session_id: str = Body(..., embed=True)):
    presenter = HTTPPresenter()
    use_case = container.get_finish_counseling_use_case(presenter)
    use_case.execute(FinishCounselingInputDTO(session_id=session_id))
    return presenter.data

@app.get("/history/{user_id}")
def get_history(user_id: str):
    presenter = HTTPPresenter()
    use_case = container.get_manage_history_use_case(presenter)
    use_case.execute(ManageHistoryInputDTO(user_id=user_id))
    return presenter.data

# Mount static files and serve index.html
app.mount("/static", StaticFiles(directory=static_dir), name="static")

@app.get("/")
def read_index():
    return FileResponse(os.path.join(static_dir, "index.html"))

# Ensure static assets are served from current dir relative if hosted elsewhere
@app.get("/{file_path:path}")
async def serve_file(file_path: str):
    full_path = os.path.join(static_dir, file_path)
    if os.path.isfile(full_path):
        return FileResponse(full_path)
    return FileResponse(os.path.join(static_dir, "index.html"))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
