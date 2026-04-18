from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from shared.dependencies import get_db
from sqlalchemy import select
from project_taskify.models.task_model import Task
from typing import List
from shared.exception import NotFound
from project_taskify.schemas.schema import TaskRequest, TaskResponse

router = APIRouter(prefix='/tasks', tags=["Lista de tarefas"])

async def get_task_or_404(id_task: int, 
                          db: AsyncSession) -> Task:
      task = await db.get(Task, id_task)
      if task is None:
        raise NotFound(name="")
      
      return task

#endpoint para obter todas as tarefas
@router.get("", response_model=List[TaskResponse])
async def get_all_task(db: AsyncSession = Depends(get_db)) -> List[TaskResponse]:
    result = await  db.execute(select(Task))

    return result.scalars().all()

#endpoint para obter tarefas por id
@router.get("/{id_task}", response_model=TaskResponse)
async def get_task_by_id(id_task: int,
                        db: AsyncSession = Depends(get_db)) -> TaskResponse:
    return await get_task_or_404(id_task, db)

#endpoint para criar tarefas
@router.post("", response_model=TaskResponse, status_code=201)
async def create_task(task_request: TaskRequest,
                     db: AsyncSession = Depends(get_db)) -> TaskResponse:

    task = Task(
        **task_request.model_dump() 
    )
    
    db.add(task) 
    await db.commit() 
    await db.refresh(task) 
    return task 

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

#endpoint para finalizar tarefas
@router.patch("/finish/{id_task}", response_model=TaskResponse, status_code=200)
async def finish_task_by_id(id_task: int, 
                      db: AsyncSession = Depends(get_db)) -> TaskResponse:
    task = await get_task_or_404(id_task, db)

    if task.completed:
        raise HTTPException(status_code=400, detail="Tarefa já foi finalizada!")

    task.completed = True
    
    await db.commit()
    await db.refresh(task)
    return task

#endpoint para apagar tarefas
@router.delete("/{id_task}", status_code=204)
async def delete_task_by_id(id_task: int,
                     db: AsyncSession = Depends(get_db)) -> None:
    task = await get_task_or_404(id_task, db)

    await db.delete(task)
    await db.commit()
