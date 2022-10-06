from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

#Test api IsPrime
def test_IsPrime() :
    response = client.get('/isprime/2')
    assert response.status_code == 200
    assert response.json() == (True)

def test_IsPrimeError() :
    response = client.get('/isprime/4')
    assert response.status_code == 200
    assert response.json() == (True)

#Test api fibonacci
#Test pass
def test_fibonacci() :
    response = client.get('/fibonacci/4')
    assert response.status_code == 200
    assert response.json() == (2)

#Test Error
def test_fibonacci1() :
    response = client.get('/fibonacci/3')
    assert response.status_code == 200
    assert response.json() == (1)