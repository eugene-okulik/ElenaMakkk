import pytest
import requests
from test_api_emakovskaya.endpoints.create_object import Create_object
from test_api_emakovskaya.endpoints.update_object import UpdateObject
from test_api_emakovskaya.endpoints.get_objects import GetObjects
from test_api_emakovskaya.endpoints.get_object import GetObject
from test_api_emakovskaya.endpoints.patch_object import PatchObject
from test_api_emakovskaya.endpoints.delete_object import DeleteObject


@pytest.fixture()
def create_object_endpoint():
    return Create_object()


@pytest.fixture()
def put_object_endpoint():
    return UpdateObject()


@pytest.fixture()
def get_objects_endpoint():
    return GetObjects()


@pytest.fixture()
def get_object_endpoint():
    return GetObject()


@pytest.fixture()
def patch_object_endpoint():
    return PatchObject()


@pytest.fixture()
def delete_object_endpoint():
    return DeleteObject()


@pytest.fixture()
def new_object_id():
    url = 'http://objapi.course.qa-practice.com/object'
    body = {
        "name": "Elena",
        "data": {
            "level": 1,
            "group": 357
        }
    }
    response = requests.post(url, json=body).json()
    object_id = response['id']
    yield object_id
    requests.delete(f'{url}/{object_id}')
