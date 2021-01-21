import requests
import json


def test_get_all():
    url = 'http://127.0.0.1:5000/group'
    headers = {
        'Content-Type': 'application/json'
    }
    rv = requests.get(url, headers=headers)
    assert rv.status_code == 200

def test_get():
    url = 'http://127.0.0.1:5000/group/1'
    headers = {
        'Content-Type': 'application/json'
    }
    rv = requests.get(url, headers=headers)
    assert rv.status_code == 200

def test_post():
    url = 'http://127.0.0.1:5000/group/'
    headers = {
        'Content-Type': 'application/json'
    }
    group_dict = {
            "id": 10,
            "name": "ADM",
            "certificado_id": 1
    } 
    rv = requests.request('POST', url, headers=headers, data=json.dumps(group_dict))
    assert rv.status_code == 200 or rv.status_code == 400

def test_put():
    url = 'http://127.0.0.1:5000/group/10'
    headers = {
        'Content-Type': 'application/json'
    }
    group_dict = {
            "name": "ADM",
            "certificado_id": 1
    } 
    rv = requests.request('PUT', url, headers=headers, data=json.dumps(group_dict))
    assert rv.status_code == 200 or rv.status_code == 201

def test_delete():
    url = 'http://127.0.0.1:5000/group/10'
    headers = {
        'Content-Type': 'application/json'
    }
    rv = requests.request('DELETE', url, headers=headers)
    assert rv.status_code == 200
