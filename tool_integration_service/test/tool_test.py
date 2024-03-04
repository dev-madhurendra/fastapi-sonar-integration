from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
import os
import sys
sys.path.append(os.getcwd())
from db.db import Base
from main import app

SQLALCHEMY_DATABASE_URL = "sqlite://"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        

Base.metadata.create_all(bind=engine)

client = TestClient(app)

def test_create_tool():
    tool_data = {
        "tool_name": "Test Tool",
        "src": "Test Source",
        "is_enabled": True
    }
    response = client.post("/api/v1/tools", json=tool_data)
    assert response.status_code == 200
    assert response.json()["tool_name"] == "Test Tool"
    assert response.json()["src"] == "Test Source"
    assert response.json()["is_enabled"] is True

def test_get_all_tools():
    response = client.get("/api/v1/tools")
    assert response.status_code == 200
    assert len(response.json()) > 0

    response = client.get("/api/v1/tools?tool_name=Test Tool")
    assert response.status_code == 200
    assert len(response.json()) == 1


def test_get_tool_by_id():
    response = client.get("/api/v1/tools/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1

def test_update_tool():
    tool_data = {
        "tool_name": "Updated Tool",
        "src": "Updated Source",
        "is_enabled": False
    }
    response = client.put("/api/v1/tools/1", json=tool_data)
    assert response.status_code == 200
    assert response.json()["tool_name"] == "Updated Tool"
    assert response.json()["src"] == "Updated Source"
    assert response.json()["is_enabled"] is False

def test_delete_tool():
    response = client.delete("/api/v1/tools/1")
    assert response.status_code == 200
    assert response.json()["detail"] == "Tool 1 deleted successfully!"
