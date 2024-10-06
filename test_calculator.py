import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_add(client):
    response = client.post('/add', json={'a': 5, 'b': 3})
    assert response.get_json()['result'] == 8

def test_subtract(client):
    response = client.post('/subtract', json={'a': 5, 'b': 3})
    assert response.get_json()['result'] == 2

def test_multiply(client):
    response = client.post('/multiply', json={'a': 5, 'b': 3})
    assert response.get_json()['result'] == 15

def test_divide(client):
    response = client.post('/divide', json={'a': 6, 'b': 3})
    assert response.get_json()['result'] == 2

def test_divide_by_zero(client):
    response = client.post('/divide', json={'a': 6, 'b': 0})
    assert response.status_code == 400

def test_sqrt(client):
    response = client.post('/sqrt', json={'a': 9})
    assert response.get_json()['result'] == 3

def test_sqrt_negative(client):
    response = client.post('/sqrt', json={'a': -9})
    assert response.status_code == 400
