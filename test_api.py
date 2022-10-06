from fastapi.testclient import TestClient


client = TestClient()

#Test api IsPrime
def test_IsPrime() :
    response = client.get('/IsPrime/2')
    assert response.status_code == 200
    assert response.json() == (True)
