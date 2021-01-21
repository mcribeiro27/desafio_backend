import requests
import json


def test_get_all():
    url = 'http://127.0.0.1:5000/certificado'
    headers = {
        'Content-Type': 'application/json'
    }
    rv = requests.get(url, headers=headers)

    assert rv.status_code == 200

def test_get():
    url = 'http://127.0.0.1:5000/certificado/1'
    headers = {
        'Content-Type': 'application/json'
    }
    rv = requests.get(url, headers=headers)

    assert rv.status_code == 200

def test_get_by_username():
    url = 'http://127.0.0.1:5000/certificado/mcribeiro'
    headers = {
        'Content-Type': 'application/json'
    }
    rv = requests.get(url, headers=headers)

    assert rv.status_code == 200

def test_post():
    url = 'http://127.0.0.1:5000/certificado/'
    headers = {
            'Content-Type': 'application/json'
    }
    post_dict = {   
            "id": 10,
            "username": "mcribeiro",
            "name": "marcos cesar",
            "description": "123456",
            "expiration": 50,
            "expirated_at": "20/03/2021"
    }

    rv = requests.request('POST', url, headers=headers, data=json.dumps(post_dict))
    assert rv.status_code == 200 or rv.status_code == 400

def test_put():
    url = 'http://127.0.0.1:5000/certificado/10'
    headers = {
            'Content-Type': 'application/json'
    }
    post_dict = {   
            "username": "mcribeiro27",
            "name": "marcos cesar",
            "description": "123456",
            "expiration": 50,
            "expirated_at": "20/03/2021"
    }

    rv = requests.request('PUT', url, headers=headers, data=json.dumps(post_dict))
    assert rv.status_code == 200 or rv.status_code == 400

def test_delete():
    url = 'http://127.0.0.1:5000/certificado/10'
    headers = {
        'Content-Type': 'application/json'
    }
    rv = requests.request('DELETE', url, headers=headers)
    assert rv.status_code == 200