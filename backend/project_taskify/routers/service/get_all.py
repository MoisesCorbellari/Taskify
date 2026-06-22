from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from shared.dependencies import get_db
from project_taskify.models.task_model import Task
from project_taskify.schemas.schema import TaskResponse

router = APIRouter()


# endpoint para obter todas as tarefas
@router.get("/", response_model=List[TaskResponse])
async def get_all_task(db: AsyncSession = Depends(get_db)) -> List[TaskResponse]:
    result = await db.execute(select(Task))

    return result.scalars().all()
