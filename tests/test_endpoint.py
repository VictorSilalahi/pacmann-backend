import requests

token = None

def test_user_list():
    r = requests.get("http://127.0.0.1:5000/api/users")
    assert r.status_code == 200

def test_login_with_registered_user():
    global token
    r = requests.post("http://127.0.0.1:5000/api/user/validate", data={'email': 'wendi@gmail.com', 'password': 'wendi123'})
    content = r.json()
    token = content['token']    
    assert r.status_code == 200


def test_login_with_non_registered_user():
    r = requests.post("http://127.0.0.1:5000/api/user/validate", data={'email': 'we@gmail.com', 'password': 'wen'})
    assert r.status_code == 401

def test_todo_list_with_token():
    r = requests.get("http://127.0.0.1:5000/api/todo", headers={'Authorization': 'Bearer '+token})
    assert r.status_code == 200

def test_todo_list_without_token():
    r = requests.get("http://127.0.0.1:5000/api/todo")
    assert r.json() == None
