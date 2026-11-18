
from fastapi.testclient import TestClient
from main import app

client = TestClient(app) #creates a test client for the FastAPI application.


def test_home():
    response = client.get("/")

    assert response.status_code == 200 # checks if the response status code is 200 (OK).
    assert response.json()["message"] == "Task Management API is running!" #	Reads the response data
