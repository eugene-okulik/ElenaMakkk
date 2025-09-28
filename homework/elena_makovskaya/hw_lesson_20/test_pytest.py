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


# Получение списка всех объектов
@pytest.mark.medium
def test_get_objects(start_end_testing, start_end_test):
    response = requests.get(url)
    assert response.status_code == 200, 'status code is not correct'


@pytest.mark.critical
# Получение одного объекта по id
def test_get_object(new_object_id, start_end_test):
    response = requests.get(f'{url}/{new_object_id}')
    assert response.json()['id'] == new_object_id


# Добавление нового объекта
@pytest.mark.parametrize('name', ['Elena_1', 'Elena_2', 'Elena_3'])
def test_post_object(name, start_end_test):
    body = {
        "name": name,
        "data": {
            "level": 1,
            "group": 357
        }
    }
    response = requests.post(url, json=body)
    assert response.json()['name'] == name


# Изменение существующего объекта (put)
def test_put_object(new_object_id, start_end_test):
    body = {
        "name": "Elena2",
        "data": {
            "level": 2,
            "group": 2
        }
    }
    response = requests.put(f'{url}/{new_object_id}', json=body)
    assert response.status_code == 200, 'Неверный статус код'
    assert response.json()['name'] == 'Elena2', 'В ответе вернулся неверный параметр name'


# Изменение существующего объекта (patch)
def test_patch_object(new_object_id, start_end_test):
    body = {
        "name": "Elena3"
    }
    response = requests.patch(f'{url}/{new_object_id}', json=body)
    assert response.status_code == 200, 'Неверный статус код'
    assert response.json()['name'] == 'Elena3', 'В ответе вернулся неверный параметр name'


# Удаление объекта
def test_delete_object(new_object_id, start_end_test):
    response = requests.delete(f'{url}/{new_object_id}')
    assert response.status_code == 200, 'Неверный статус код'
