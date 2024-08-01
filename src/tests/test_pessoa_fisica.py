import json
import pytest
from src.settings.server import create_app

app = create_app()


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_sacar_pessoa_fisica(client):
    response = client.post('/pessoa_fisica/1/sacar', json={'valor': 500})
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['message'] == "Saque realizado com sucesso"


def test_extrato_pessoa_fisica(client):
    response = client.get('/pessoa_fisica/1/extrato')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'id' in data
    assert 'saldo' in data
