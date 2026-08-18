from fastapi import APIRouter
from shared.types import DbSession

from app.models.task_model import Task
from app.schemas.schema import TaskRequest, TaskResponse

router = APIRouter()


# endpoint para criar tarefas
@router.post("/", response_model=TaskResponse, status_code=201)
async def create_task(
    task_request: TaskRequest, db: DbSession
) -> TaskResponse:

    task = Task(**task_request.model_dump())

    db.add(task)
    await db.commit()
    await db.refresh(task)
    return task
