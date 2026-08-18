from fastapi import APIRouter

from .router.create import router as create_router
from .router.delete import router as delete_router
from .router.finish import router as finish_router
from .router.get_all import router as get_all_router
from .router.get_id import router as get_by_id_router
from .router.update import router as update_router

router = APIRouter(prefix="/tasks", tags=["Lista de tarefas"])

router.include_router(get_all_router)
router.include_router(get_by_id_router)
router.include_router(create_router)
router.include_router(update_router)
router.include_router(finish_router)
router.include_router(delete_router)
