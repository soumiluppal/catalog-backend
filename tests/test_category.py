import os
import tempfile
from flask import jsonify
import json

import pytest

from app import flaskapp

def test_get_category(client, init_db):
    response = client.get('/categories')
    assert response.status_code == 200
    assert b"Category 1" in response.data

def test_pass_post_category(client, init_db):
    headers = {
        'Content-Type': 'application/json'
    }
    data = {
        'name': 'Category 3',
        'description': 'Test category number 3'
    }
    response = client.post('/categories', data=json.dumps(data), headers=headers)
    assert response.status_code == 201
    assert b"Category 3" in response.data

def test_fail_post_category(client, init_db):
    headers = {
        'Content-Type': 'application/json'
    }
    data = {
        'name': 'Category 1',
        'description': 'Test category number 3'
    }
    response = client.post('/categories', data=json.dumps(data), headers=headers)
    assert response.status_code == 400