from fastapi import APIRouter, Depends, HTTPException
from shared.dependencies import get_db
from sqlalchemy.orm import Session
from project_taskify.models.task_model import Task
from typing import List
from shared.exception import NotFound
from project_taskify.schemas.schema import TaskRequest, TaskResponse

router = APIRouter(prefix='/task', tags=["Lista de tarefas"])

def find_task_by_id(id_task: int, db: Session) -> Task:
    task = db.get(Task, id_task)
    if task is None:
        raise NotFound(name="")
    
    return task

#endpoint para obter todas as tarefas
@router.get("/get-all", response_model=List[TaskResponse])
def get_all_task(db: Session = Depends(get_db)) -> List[TaskResponse]:
    return db.query(Task).all()

#endpoint para obter tarefas por id
@router.get("/get-by-id/{id_task}", response_model=TaskResponse)
def get_task_by_id(id_task: int,
                        db: Session = Depends(get_db)) -> List[TaskResponse]:
    task: Task = find_task_by_id(id_task, db)
    return task

#endpoint para criar tarefas
@router.post("/create", response_model=TaskResponse, status_code=201)
def create_task(task_request: TaskRequest,
                     db: Session = Depends(get_db)) -> TaskResponse:

    task = Task(
        **task_request.model_dump() 
    )
    
    db.add(task) 
    db.commit() 
    db.refresh(task) 
    return task 

#endpoint para atualizar tarefas
@router.put("/update-by-id/{id_task}", response_model=TaskResponse, status_code=200)
def update_task_by_id(id_task: int,
                            task_request: TaskRequest,
                            db: Session = Depends(get_db)) -> TaskResponse:
    task = find_task_by_id(id_task, db)
    
    task.title = task_request.title
    task.description = task_request.description
    task.completed = task_request.completed
    
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

#endpoint para finalizar tarefas
@router.post("/finish-by-id/{id_task}", response_model=TaskResponse, status_code=200)
def finish_task_by_id(id_task: int, db: Session = Depends(get_db)) -> TaskResponse:
    task = find_task_by_id(id_task, db)

    if task.completed:
        raise HTTPException(status_code=400, detail="Tarefa já foi finalizada!")

    task.completed = True
    
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

#endpoint para apagar tarefas
@router.delete("/delete-by-id/{id_task}", status_code=204)
def delete_task_by_id(id_task: int,
                     db: Session = Depends(get_db)) -> None:
    task = find_task_by_id(id_task, db)

    db.delete(task)
    db.commit()


