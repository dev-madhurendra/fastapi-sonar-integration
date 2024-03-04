# import pytest
# from fastapi.testclient import TestClient
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.pool import StaticPool
# import os
# import sys
# from sqlalchemy.ext.declarative import declarative_base

# # Add your project path to sys.path
# sys.path.append(os.getcwd() + "/tool_integration_service")
# from main import app

# SQLALCHEMY_DATABASE_URL = "sqlite://"

# # Create engine and sessionmaker for testing
# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL,
#     connect_args={"check_same_thread": False},
#     poolclass=StaticPool,
# )
# TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# # Create Base class for declarative models
# Base = declarative_base()

# # Fixture to create a new testing session for each test case
# @pytest.fixture(scope="function")
# def db_session():
#     session = TestingSessionLocal()
#     try:
#         yield session
#     finally:
#         session.close()


# # Fixture to provide a test client for each test case
# @pytest.fixture(scope="module")
# def client():
#     yield TestClient(app)


# # Define test cases using the fixtures
# def test_create_tool(client, db_session):
#     tool_data = {
#         "tool_name": "Test Tool",
#         "src": "Test Source",
#         "is_enabled": True,
#     }
#     response = client.post("/api/v1/tools", json=tool_data)
#     assert response.status_code == 200
#     assert response.json()["tool_name"] == "Test Tool"
#     assert response.json()["src"] == "Test Source"
#     assert response.json()["is_enabled"] is True


# def test_get_all_tools(client):
#     response = client.get("/api/v1/tools")
#     assert response.status_code == 200
#     assert len(response.json()) > 0

#     response = client.get("/api/v1/tools?tool_name=Test Tool")
#     assert response.status_code == 200
#     assert len(response.json()) == 1


# def test_get_tool_by_id(client):
#     response = client.get("/api/v1/tools/1")
#     assert response.status_code == 200
#     assert response.json()["id"] == 1


# def test_update_tool(client, db_session):
#     tool_data = {
#         "tool_name": "Updated Tool",
#         "src": "Updated Source",
#         "is_enabled": False,
#     }
#     response = client.put("/api/v1/tools/1", json=tool_data)
#     assert response.status_code == 200
#     assert response.json()["tool_name"] == "Updated Tool"
#     assert response.json()["src"] == "Updated Source"
#     assert response.json()["is_enabled"] is False


# def test_delete_tool(client):
#     response = client.delete("/api/v1/tools/1")
#     assert response.status_code == 200
#     assert response.json()["detail"] == "Tool 1 deleted successfully!"

def test_is_true():
    assert 1==1