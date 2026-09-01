import os

import logfire
from app.api.api_router import router
from fastapi import FastAPI
from shared.exception import NotFound
from shared.exceptions_handler import not_found_exception_handler
from uvicorn import run

logfire.configure(token=os.environ["LOGFIRE_TOKEN"])

app = FastAPI(
    title="Taskify - API para lista de tarefas!",
    description="""
    API para gerenciamento de tarefas, fornece endpoints para operações CRUD (Create, Read, Update, Delete), além de um endpoint específico para finalizar tarefas.
    """,
)



@app.get(
    "/",
    summary="Página inicial",
)
def todo_list() -> str:
    return "Taskify - Lista de tarefas"

app.include_router(router)
app.add_exception_handler(NotFound, not_found_exception_handler)
logfire.instrument_fastapi(app)

if __name__ == "__main__":
    run("main:app", host="0.0.0.0", port=8000)
