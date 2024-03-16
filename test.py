import app
import json
import warnings

def test_hello_world():
    response = app.app.test_client().get('/hello')
    assert response.status_code == 200
    assert response.data == b'Hello'

def test_goodbye():
    response = app.app.test_client().get('/goodbye')
    assert response.status_code == 404

def test_age():
    response = app.app.test_client().get('/age')
    assert response.status_code == 200
    assert response.data == b'20'