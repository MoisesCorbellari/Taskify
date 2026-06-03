from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from shared.dependencies import get_db, get_task_or_404
from project_taskify.schemas.schema import TaskResponse

router = APIRouter()

#endpoint para obter tarefas por id
@router.get("/{id_task}", response_model=TaskResponse)
async def get_task_by_id(id_task: int,
                        db: AsyncSession = Depends(get_db)
                        ) -> TaskResponse:
    return await get_task_or_404(id_task, db)