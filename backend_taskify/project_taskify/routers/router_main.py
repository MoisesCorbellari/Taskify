from fastapi import APIRouter
from .service.get_all import router as get_all_router
from .service.get_id import router as get_by_id_router
from .service.create import router as create_router
from .service.update import router as update_router
from .service.finish import router as finish_router
from .service.delete import router as delete_router



router = APIRouter(
    prefix='/tasks', 
    tags=["Lista de tarefas"]
    )

router.include_router(get_all_router)
router.include_router(get_by_id_router)
router.include_router(create_router)
router.include_router(update_router)
router.include_router(finish_router)
router.include_router(delete_router)