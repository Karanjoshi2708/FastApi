from fastapi.testclient import TestClient
from main_test_api import app

client = TestClient(app)


#test home api
def test_home():
    response = client.get("/")
    #check status code
    assert response.status_code == 200
    assert response.json() == {"message": "hello karan !!!"}

#test add api
def test_add():
    response = client.get("/add?a=5&b=10")
    #check status code
    assert response.status_code == 200
    assert response.json() == {"result": 15}