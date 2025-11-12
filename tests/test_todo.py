from app.main import app, todos  # ← импортируем список, чтобы очищать его
from fastapi.testclient import TestClient


client = TestClient(app)


def setup_function():
    todos.clear()  # очищаем перед каждым тестом


def test_create_and_get():
    data = {"id": 1, "title": "Test task"}
    r = client.post("/todos", json=data)
    assert r.status_code == 200
    assert r.json()["title"] == "Test task"
    assert r.json()["done"] is False

    r = client.get("/todos")
    assert len(r.json()) == 1


def test_toggle():
    data = {"id": 2, "title": "Second"}
    r = client.post("/todos", json=data)
    assert r.status_code == 200

    r = client.patch("/todos/2")
    assert r.status_code == 200
    assert r.json()["done"] is True
