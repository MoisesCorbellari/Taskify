from fastapi import APIRouter
from .service.get_all import router as get_all_task
from .service.get_id import router as get_task_by_id
from .service.create import router as create_task
from .service.update import router as update_task_by_id
from .service.finish import router as finish_task_by_id
from .service.delete import router as delete_task_by_id



router = APIRouter(
    prefix='/tasks', 
    tags=["Lista de tarefas"]
    )

router.include_router(get_all_task)
router.include_router(get_task_by_id)
router.include_router(create_task)
router.include_router(update_task_by_id)
router.include_router(finish_task_by_id)
router.include_router(delete_task_by_id)