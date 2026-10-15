import pytest
from httpx import ASGITransport, AsyncClient
from main import app
from shared.database import Base
from shared.dependencies import get_db
from sqlalchemy.ext.asyncio import (
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.pool import StaticPool


@pytest.fixture
def anyio_backend():
    return "asyncio"


@pytest.fixture
async def client(anyio_backend):
    engine = create_async_engine(
        "sqlite+aiosqlite://",
        poolclass=StaticPool
    )

    TestSessionLocal = async_sessionmaker(
        bind=engine,
        autoflush=False,
        expire_on_commit=False,
    )

    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)

    async def override_get_db():
        async with TestSessionLocal() as session:
            yield session

    app.dependency_overrides[get_db] = override_get_db

    try:
        async with AsyncClient(
            transport=ASGITransport(app=app),
            base_url="http://test",
        ) as test_client:
            yield test_client
    finally:
        app.dependency_overrides.pop(get_db, None)

        async with engine.begin() as connection:
            await connection.run_sync(Base.metadata.drop_all)

        await engine.dispose()

@pytest.mark.anyio
async def test_list_tasks(client):
    response = await client.get("/tasks/")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


@pytest.mark.anyio
async def test_create_task(client):
    payload = {
        "title": "Estudar Python",
        "description": "Revisar FastAPI",
    }

    response = await client.post("/tasks/", json=payload)

    assert response.status_code == 201

    data = response.json()
    assert data["title"] == payload["title"]
    assert data["description"] == payload["description"]
    assert "id" in data


@pytest.mark.anyio
async def test_get_task(client):
    payload = {
        "title": "Estudar Python",
        "description": "Revisar FastAPI",
    }

    created = await client.post("/tasks/", json=payload)
    assert created.status_code == 201

    task_id = created.json()["id"]
    response = await client.get(f"/tasks/{task_id}")

    assert response.status_code == 200
    assert response.json()["id"] == task_id
    assert response.json()["title"] == payload["title"]


@pytest.mark.anyio
async def test_update_task(client):
    created = await client.post(
        "/tasks/",
        json={
            "title": "Título antigo",
            "description": "Descrição antiga",
        },
    )
    assert created.status_code == 201

    task_id = created.json()["id"]
    payload = {
        "title": "Título atualizado",
        "description": "Descrição atualizada",
    }

    response = await client.put(
        f"/tasks/{task_id}",
        json=payload,
    )

    assert response.status_code == 200
    assert response.json()["title"] == payload["title"]
    assert response.json()["description"] == payload["description"]


@pytest.mark.anyio
async def test_finish_task(client):
    created = await client.post(
        "/tasks/",
        json={
            "title": "Finalizar tarefa",
            "description": "Testar conclusão",
        },
    )
    assert created.status_code == 201

    task_id = created.json()["id"]
    response = await client.patch(f"/tasks/finish/{task_id}")

    assert response.status_code == 200
    assert response.json()["completed"] is True


@pytest.mark.anyio
async def test_finish_task_twice(client):
    created = await client.post(
        "/tasks/",
        json={
            "title": "Finalizar duas vezes",
            "description": "Testar erro",
        },
    )
    assert created.status_code == 201

    task_id = created.json()["id"]

    first_response = await client.patch(
        f"/tasks/finish/{task_id}"
    )
    second_response = await client.patch(
        f"/tasks/finish/{task_id}"
    )

    assert first_response.status_code == 200
    assert second_response.status_code == 400
    assert second_response.json()["detail"] == (
        "Tarefa já foi finalizada!"
    )


@pytest.mark.anyio
async def test_delete_task(client):
    created = await client.post(
        "/tasks/",
        json={
            "title": "Excluir tarefa",
            "description": "Testar exclusão",
        },
    )
    assert created.status_code == 201

    task_id = created.json()["id"]
    response = await client.delete(f"/tasks/{task_id}")

    assert response.status_code == 204

    get_response = await client.get(f"/tasks/{task_id}")
    assert get_response.status_code == 404