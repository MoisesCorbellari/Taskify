from fastapi import FastAPI
from project_taskify.routers.main_router import router
from shared.exception import NotFound
from shared.exceptions_handler import not_found_exception_handler
from uvicorn import run

app = FastAPI(
    title="Taskify - Lista de Tarefas!",
    description="""
    API para gerenciamento de tarefas, fornece endpoints para operações CRUD (Create, Read, Update, Delete), além de um endpoint específico para finalizar tarefas.
    """,
)


@app.get(
    "/",
    summary="Página inicial da API",
)
def todo_list() -> str:
    return "Taskify - API para Lista de Tarefas!"


app.include_router(router)
app.add_exception_handler(NotFound, not_found_exception_handler)

if __name__ == "__main__":
    run("main:app", host="0.0.0.0", port=8000)
