from fastapi import APIRouter

from app.schemas.schema import TaskRequest, TaskResponse
from shared.alias import DbSession
from shared.dependencies import get_task_or_404

router = APIRouter()


# endpoint para atualizar tarefas
@router.put("/{id_task}", response_model=TaskResponse, status_code=200)
async def update_task_by_id(
    id_task: int, task_request: TaskRequest, db: DbSession
) -> TaskResponse:
    task = await get_task_or_404(id_task, db)

    task.title = task_request.title
    task.description = task_request.description
    task.completed = task_request.completed

    await db.commit()
    await db.refresh(task)
    return task
