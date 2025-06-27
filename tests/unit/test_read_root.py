from http import HTTPStatus

from fastapi.testclient import TestClient

from itau_api.main import app

client = TestClient(app)


def test_read_root():
    response = client.get('/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Server is running!'}
