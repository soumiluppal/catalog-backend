import os
import tempfile
from flask import jsonify
import json

import pytest

from app import flaskapp

def login(client):
    headers = {
        'Content-Type': 'application/json'
    }
    data = {
        'username': 'testuser1',
        'password': 'testpassword123'
    }
    response = client.post('/auth', data=json.dumps(data), headers=headers)
    return json.loads(response.data)['access_token']

def test_pass_get_items(client, init_db):
    response = client.get('/categories/1/items')
    assert response.status_code == 200
    assert b"Item 1" in response.data

def test_fail_get_items(client, init_db):
    response = client.get('/categories/5/items')
    assert response.status_code == 404

def test_fail_new_item_auth(client, init_db):
    response = client.post('/categories/1/items', data={})
    assert response.status_code == 401

def test_fail_new_item_bad(client, init_db):
    headers = {
        'Authorization': 'JWT ' + str(login(client)),
        'Content-Type': 'application/json'
    }
    data = {
        'name': 'Item new',
        'description': 'Test item new'
    }
    response = client.post('/categories/1/items', data=json.dumps(data), headers=headers)
    assert response.status_code == 400

def test_fail_new_item_category(client, init_db):
    headers = {
        'Authorization': 'JWT ' + str(login(client)),
        'Content-Type': 'application/json'
    }
    data = {
        'name': 'Item new',
        'description': 'Test item new',
        'price': 10
    }
    response = client.post('/categories/5/items', data=json.dumps(data), headers=headers)
    assert response.status_code == 404

def test_pass_new_item(client, init_db):
    headers = {
        'Authorization': 'JWT ' + str(login(client)),
        'Content-Type': 'application/json'
    }
    data = {
        'name': 'Item new',
        'description': 'Test item new',
        'price': 10
    }
    response = client.post('/categories/1/items', data=json.dumps(data), headers=headers)
    assert response.status_code == 201

def test_fail_change_item(client, init_db):
    headers = {
        'Content-Type': 'application/json'
    }
    data = {
        'name': 'Item 1 changed',
        'description': 'Test item 1',
        'price': 10
    }
    response = client.put('/categories/1/items/1', data=json.dumps(data), headers=headers)
    assert response.status_code == 401

def test_pass_change_item(client, init_db):
    headers = {
        'Authorization': 'JWT ' + str(login(client)),
        'Content-Type': 'application/json'
    }
    data = {
        'name': 'Item 1 changed',
        'description': 'Test item 1',
        'price': 10
    }
    response = client.put('/categories/1/items/1', data=json.dumps(data), headers=headers)
    assert response.status_code == 200

def test_fail_delete_item(client, init_db):
    headers = {
        'Content-Type': 'application/json'
    }
    response = client.delete('/categories/1/items/1', headers=headers)
    assert response.status_code == 401

def test_pass_delete_item(client, init_db):
    headers = {
        'Authorization': 'JWT ' + str(login(client)),
        'Content-Type': 'application/json'
    }
    response = client.delete('/categories/1/items/1', headers=headers)
    assert response.status_code == 200