from fastapi import APIRouter
from shared.types import DbSession
from sqlalchemy import select

from app.models.task_model import Task
from app.schemas.schema import TaskResponse

router = APIRouter()


# endpoint para obter todas as tarefas
@router.get("/", response_model=list[TaskResponse])
async def get_all_task(db: DbSession) -> list[TaskResponse]:
    result = await db.execute(select(Task))

    return result.scalars().all()
