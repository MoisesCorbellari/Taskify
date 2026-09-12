from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from shared.dependencies import get_db

# Alias que combina AsyncSession com Depends(get_db), simplificando
# a injeção da sessão do banco nas rotas e serviços.
DbSession = Annotated[AsyncSession, Depends(get_db)]
