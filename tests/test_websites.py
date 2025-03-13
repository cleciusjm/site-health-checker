from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_should_read_empty_websites():
    response = client.get("/websites")
    assert response.status_code == 200
    assert response.json() == []
    
def test_should_write_and_read_first_website():
    body = { "url":"https://test.com" }
    response = client.post("/websites", json=body)
    assert response.status_code == 200
    assert response.json() == {**body, "active":True}    
    
    listResponse = client.get("/websites")
    assert listResponse.status_code == 200
    assert listResponse.json() == [{**body, "active":True}]