from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from shared.dependencies import get_db
from project_taskify.models.task_model import Task
from project_taskify.schemas.schema import TaskRequest, TaskResponse

router = APIRouter()


# endpoint para criar tarefas
@router.post("/", response_model=TaskResponse, status_code=201)
async def create_task(
    task_request: TaskRequest, db: AsyncSession = Depends(get_db)
) -> TaskResponse:

    task = Task(**task_request.model_dump())

    db.add(task)
    await db.commit()
    await db.refresh(task)
    return task
