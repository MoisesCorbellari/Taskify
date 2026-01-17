from fastapi import APIRouter, Depends, HTTPException
from shared.dependencies import get_db
from sqlalchemy.orm import Session
from project_do_up.models.do_up_model import DoUp
from typing import List
from shared.exception import NotFound
from project_do_up.schemas.schema import Do_Up_Request, Do_Up_Response

router = APIRouter(prefix='/DoUp', tags=["Lista de tarefas"])

def find_do_up_by_id(id_task: int, db: Session) -> DoUp:
    do_up = db.get(DoUp, id_task)
    if do_up is None:
        raise NotFound(name="")
    
    return do_up

#endpoint para obter todas as tarefas
@router.get("/get-all", response_model=List[Do_Up_Response])
def get_all_do_up(db: Session = Depends(get_db)) -> List[Do_Up_Response]:
    return db.query(DoUp).all()

#endpoint para obter tarefas por id
@router.get("/get-by-id/{id_task}", response_model=Do_Up_Response)
def get_do_up_by_id(id_task: int,
                        db: Session = Depends(get_db)) -> List[Do_Up_Response]:
    do_up: DoUp = find_do_up_by_id(id_task, db)
    return do_up

#endpoint para criar tarefas
@router.post("/create", response_model=Do_Up_Response, status_code=201)
def create_do_up(task_request: Do_Up_Request,
                     db: Session = Depends(get_db)) -> Do_Up_Response:

    do_up = DoUp(
        **task_request.model_dump() 
    )
    
    db.add(do_up) 
    db.commit() 
    db.refresh(do_up) 
    return do_up 

#endpoint para atualizar tarefas
@router.put("/update/{id_task}", response_model=Do_Up_Response, status_code=200)
def update_do_up_by_id(id_task: int,
                            task_request: Do_Up_Request,
                            db: Session = Depends(get_db)) -> Do_Up_Response:
    do_up = find_do_up_by_id(id_task, db)
    
    do_up.title = task_request.title
    do_up.description = task_request.description
    do_up.completed = task_request.completed
    
    db.add(do_up)
    db.commit()
    db.refresh(do_up)
    return do_up

#endpoint para finalizar tarefas
@router.post("/finish/{id_task}", response_model=Do_Up_Response, status_code=200)
def finish_do_up_by_id(id_task: int, db: Session = Depends(get_db)) -> Do_Up_Response:
    do_up = find_do_up_by_id(id_task, db)

    if do_up.completed:
        raise HTTPException(status_code=400, detail="Tarefa já foi finalizada!")

    do_up.completed = True
    
    db.add(do_up)
    db.commit()
    db.refresh(do_up)
    return do_up

#endpoint para apagar tarefas
@router.delete("/delete/{id_task}", status_code=204)
def delete_do_up_by_id(id_task: int,
                     db: Session = Depends(get_db)) -> None:
    do_up = find_do_up_by_id(id_task, db)

    db.delete(do_up)
    db.commit()


