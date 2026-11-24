import os
from pathlib import Path

import logfire
from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse, RedirectResponse, Response
from fastapi.staticfiles import StaticFiles
from uvicorn import run

from app.api.api_router import router
from shared.exception import NotFound
from shared.exceptions_handler import not_found_exception_handler

logfire.configure(token=os.environ["LOGFIRE_TOKEN"])

app = FastAPI(
    title="Taskify - API para lista de tarefas",
    description="""
    API para gerenciamento de tarefas, fornece endpoints para operações CRUD (Create, Read, Update, Delete), além de um endpoint específico para finalizar tarefas.
    """,
)


@app.get("/")
async def welcome():
    return RedirectResponse(url="/app/", status_code=303)


app.include_router(router)
app.add_exception_handler(NotFound, not_found_exception_handler)
logfire.instrument_fastapi(app, excluded_urls=r".*/app(?:/.*)?")


# Trata erros de validação da requisição
@app.exception_handler(RequestValidationError)
async def request_validation_exception_handler(
    request: Request,
    exc: RequestValidationError,
) -> JSONResponse:
    details = exc.errors()

    logfire.error(
        "Falha de validação da requisição "
        f"{request.method} {request.url.path}: {details!r}"
    )
    return JSONResponse(
        status_code=422,
        content={"detail": details},
    )


# Desabilita o cache do frontend e das rotas de autenticação.
@app.middleware("http")
async def disable_frontend_caching(request: Request, call_next) -> Response:
    is_frontend_request = request.url.path == "/app" or request.url.path.startswith(
        "/app/"
    )
    if is_frontend_request:
        had_query = bool(request.scope.get("query_string"))
        request.scope["query_string"] = b""
        conditional_headers = {b"if-none-match", b"if-modified-since"}
        request.scope["headers"] = [
            (name, value)
            for name, value in request.scope["headers"]
            if name.lower() not in conditional_headers
        ]
        if had_query and request.method == "GET":
            response = RedirectResponse(url="/app/", status_code=303)
            response.headers["Cache-Control"] = "no-store"
            return response

    response = await call_next(request)
    if is_frontend_request or request.url.path.startswith("/auth/"):
        response.headers["Cache-Control"] = "no-store"
    return response


# Monta e disponibiliza os arquivos estáticos do frontend na rota /app.
app.mount(
    "/app",
    StaticFiles(directory=Path(__file__).parent / "static", html=True),
    name="frontend",
)

if __name__ == "__main__":
    run("main:app", host="0.0.0.0", port=8000)
