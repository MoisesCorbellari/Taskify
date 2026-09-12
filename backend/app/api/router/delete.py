from fastapi import APIRouter
from shared.alias import DbSession
from shared.dependencies import get_task_or_404

router = APIRouter()


# endpoint para apagar tarefas
@router.delete("/{id_task}", status_code=204)
async def delete_task_by_id(id_task: int, db: DbSession) -> None:
    task = await get_task_or_404(id_task, db)

    await db.delete(task)
    await db.commit()
