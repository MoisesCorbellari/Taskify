from fastapi import APIRouter
from shared.dependencies import get_task_or_404
from shared.types import DbSession

from app.schemas.schema import TaskResponse

router = APIRouter()


# endpoint para obter tarefas por id
@router.get("/{id_task}", response_model=TaskResponse)
async def get_task_by_id(
    id_task: int, db: DbSession
) -> TaskResponse:
    return await get_task_or_404(id_task, db)
