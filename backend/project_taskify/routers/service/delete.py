from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from shared.dependencies import get_db, get_task_or_404

router = APIRouter()


# endpoint para apagar tarefas
@router.delete("/{id_task}", status_code=204)
async def delete_task_by_id(id_task: int, db: AsyncSession = Depends(get_db)) -> None:
    task = await get_task_or_404(id_task, db)

    await db.delete(task)
    await db.commit()
