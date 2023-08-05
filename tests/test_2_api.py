from api.questions_api import api
from http import HTTPStatus
from utils.assertion import Assert
import re

def test_list_users():
    res = api.list_users()

    assert res.status_code == HTTPStatus.OK
    Assert.validate_schema(res.json())
    assert res.headers['Cache-Control'] == 'max-age=14400'

def test_single_users_not_found():
    not_found = api.single_users_not_found()

    assert not_found.status_code == HTTPStatus.NOT_FOUND
    Assert.validate_schema(not_found.json())

def test_single_user():
    single_u = api.single_user()
    res_body = single_u.json()

    assert single_u.status_code == HTTPStatus.OK
    Assert.validate_schema(single_u.json())

    assert res_body['data']['first_name'] == 'Janet'

    assert re.fullmatch(r'\w[a-z]{5}'), res_body['data']['first_name'] #варианты регулярных
    assert re.fullmatch(r'\w[a-z]+]'), res_body['data']['first_name'] #варианты регулярных
    assert re.fullmatch(r'\w+'), res_body['data']['first_name'] #варианты регулярных
    assert re.fullmatch(r'.+'), res_body['data']['first_name'] #варианты регулярных

    example = {
        "data": {
            "id": 2,
            "email": "janet.weaver@reqres.in",
            "first_name": "Janet",
            "last_name": "Weaver",
            "avatar": "https://reqres.in/img/faces/2-image.jpg"
        },
        "support": {
            "url": "https://reqres.in/#support-heading",
            "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
        }
    }
    assert example == res_body

def test_create():
    name = "Ivan"
    job = "Tester"
    res = api.create(name, job)

    assert res.status_code == HTTPStatus.CREATED
    assert res.json()['name'] == name
    assert res.json()['job'] == job
    assert re.fullmatch(r'\d{1,4}', res.json()['id'])

    assert api.delete_user(res.json()['id']).status_code == HTTPStatus.NO_CONTENT




