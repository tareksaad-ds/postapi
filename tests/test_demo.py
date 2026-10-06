from fastapi import FastAPI
from fastapi.testclient import TestClient

demo_app = FastAPI()

@demo_app.get("/hello")
def read_root():
    return {"message": "Hello World"}

client = TestClient(demo_app)

def test_homepage():
    response = client.get("/hello")
    assert response.status_code == 200
