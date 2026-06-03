from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from shared.dependencies import get_db, get_task_or_404
from project_taskify.schemas.schema import TaskRequest, TaskResponse

router = APIRouter()

#endpoint para atualizar tarefas
@router.put("/{id_task}", response_model=TaskResponse, status_code=200)
async def update_task_by_id(id_task: int,
                            task_request: TaskRequest,
                            db: AsyncSession = Depends(get_db)) -> TaskResponse:
    task = await get_task_or_404(id_task, db)
    
    task.title = task_request.title
    task.description = task_request.description
    task.completed = task_request.completed
    
    await db.commit()
    await db.refresh(task)
    return task