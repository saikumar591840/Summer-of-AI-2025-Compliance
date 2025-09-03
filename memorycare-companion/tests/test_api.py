import pytest
from fastapi.testclient import TestClient
from server.app import app

client = TestClient(app)

def test_ping():
    r = client.get('/api/ping')
    assert r.status_code == 200
    assert r.json()['status'] == 'ok'

def test_user_create_and_get():
    r = client.post('/api/users', json={'name':'Test Patient','role':'patient'})
    assert r.status_code == 200
    uid = r.json()['id']
    r = client.get(f'/api/users/{uid}')
    assert r.status_code == 200
    assert r.json()['name'] == 'Test Patient'

def test_chat_flow():
    # ensure a patient exists
    r = client.post('/api/users', json={'name':'P','role':'patient'})
    pid = r.json()['id']
    # add a memory
    r = client.post('/api/memories', json={'patient_id':pid,'title':'Picnic','content':'Family picnic at park.'})
    assert r.status_code == 200
    # chat
    r = client.post('/api/chat', json={'patient_id':pid,'message':'I feel lonely'})
    assert r.status_code == 200
    data = r.json()
    assert 'reply' in data and 'sentiment' in data
