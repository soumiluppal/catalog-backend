import os
import tempfile
from flask import jsonify
import json

import pytest

from app import flaskapp

def test_pass_login(client, init_db):
    headers = {
        'Content-Type': 'application/json'
    }
    data = {
        'username': 'testuser1',
        'password': 'testpassword123'
    }
    response = client.post('/auth', data=json.dumps(data), headers=headers)
    assert response.status_code == 200

def test_fail_login(client, init_db):
    headers = {
        'Content-Type': 'application/json'
    }
    data = {
        'username': 'testuser1',
        'password': 'testpassword12'
    }
    response = client.post('/auth', data=json.dumps(data), headers=headers)
    assert response.status_code == 401

def test_fail_register_password(client, init_db):
    headers = {
        'Content-Type': 'application/json'
    }
    data = {
        'full_name': 'New Test User',
        'email': 'testusernew@gmail.com',
        'username': 'testuser1',
        'password': 'testpassword123'
    }
    response = client.post('/user', data=json.dumps(data), headers=headers)
    assert response.status_code == 400

def test_fail_register_email(client, init_db):
    headers = {
        'Content-Type': 'application/json'
    }
    data = {
        'full_name': 'New Test User',
        'email': 'testuser1@gmail.com',
        'username': 'testusernew',
        'password': 'testpassword123'
    }
    response = client.post('/user', data=json.dumps(data), headers=headers)
    assert response.status_code == 400

def test_pass_register(client, init_db):
    headers = {
        'Content-Type': 'application/json'
    }
    data = {
        'full_name': 'New Test User',
        'email': 'testusernew@gmail.com',
        'username': 'testusernew',
        'password': 'testpassword123'
    }
    response = client.post('/user', data=json.dumps(data), headers=headers)
    assert response.status_code == 201