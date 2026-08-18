from typing import AsyncGenerator  # noqa

from sqlalchemy.ext.asyncio import AsyncSession

from app.models.task_model import Task
from shared.database import AsyncSessionLocal
from shared.exception import NotFound


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session


async def get_task_or_404(id_task: int, db: AsyncSession) -> Task:
    task = await db.get(Task, id_task)
    if task is None:
        raise NotFound(name="")

    return task
