import requests
import pytest

url = 'http://objapi.course.qa-practice.com/object'


@pytest.fixture()
def new_object_id():
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


@pytest.fixture(scope="session")
def start_end_testing():
    print('\nStart testing')
    yield
    print('\nTesting completed')


@pytest.fixture(scope="function")
def start_end_test():
    print('\nbefore test')
    yield
    print('\nafter test')
