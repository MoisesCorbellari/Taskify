from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from shared.dependencies import get_db, get_task_or_404
from project_taskify.schemas.schema import TaskResponse

router = APIRouter()


# endpoint para finalizar tarefas
@router.patch("/finish/{id_task}", response_model=TaskResponse, status_code=200)
async def finish_task_by_id(
    id_task: int, db: AsyncSession = Depends(get_db)
) -> TaskResponse:
    task = await get_task_or_404(id_task, db)

    if task.completed:
        raise HTTPException(status_code=400, detail="Tarefa já foi finalizada!")

    task.completed = True

    await db.commit()
    await db.refresh(task)
    return task
