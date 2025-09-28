import requests
import pytest
import allure

url = 'http://objapi.course.qa-practice.com/object'


@allure.title('Получение списка всех объектов')
@allure.feature('Objects')
@allure.story('Objects providing')
@pytest.mark.medium
def test_get_objects(start_end_testing, start_end_test):
    with allure.step('Отправка запроса списка всех объектов'):
        response = requests.get(url)
    with allure.step('Проверка статус код = 200'):
        assert response.status_code == 200, 'status code is not correct'


@allure.title('Получение одного объекта по id')
@pytest.mark.critical
@allure.feature('Objects')
@allure.story('Objects providing')
def test_get_object(new_object_id, start_end_test):
    with allure.step(f'Получение объекта по id {new_object_id}'):
        response = requests.get(f'{url}/{new_object_id}')
    with allure.step(f'Проверка что id из ответа = {new_object_id}'):
        assert response.json()['id'] == new_object_id


@allure.title('Добавление нового объекта')
@allure.feature('Objects')
@allure.story('Objects manipulation')
@pytest.mark.parametrize('name', ['Elena_1', 'Elena_2', 'Elena_3'])
def test_post_object(name, start_end_test):
    body = {
        "name": name,
        "data": {
            "level": 1,
            "group": 357
        }
    }
    with allure.step(f'Отправка запроса на создание нового объекта именем {name}'):
        response = requests.post(url, json=body)
    with allure.step(f'Проверка что name в ответе соответствует {name}'):
        assert response.json()['name'] == name


@allure.title('Изменение существующего объекта (put)')
@allure.feature('Objects')
@allure.story('Objects manipulation')
def test_put_object(new_object_id, start_end_test):
    body = {
        "name": "Elena2",
        "data": {
            "level": 2,
            "group": 2
        }
    }
    with allure.step(f'Отправка запроса на изменение объекта с id {new_object_id}'):
        response = requests.put(f'{url}/{new_object_id}', json=body)
    with allure.step('Проверка статус код = 200'):
        assert response.status_code == 200, 'Неверный статус код'
    with allure.step(f'Проверка что name в ответе соответствует Elena2'):
        assert response.json()['name'] == 'Elena2', 'В ответе вернулся неверный параметр name'


@allure.title('Изменение существующего объекта (patch)')
@allure.feature('Objects')
@allure.story('Objects manipulation')
def test_patch_object(new_object_id, start_end_test):
    body = {
        "name": "Elena3"
    }
    with allure.step(f'Отправка запроса на изменение объекта с id {new_object_id}'):
        response = requests.patch(f'{url}/{new_object_id}', json=body)
    with allure.step('Проверка статус код = 200'):
        assert response.status_code == 200, 'Неверный статус код'
    with allure.step(f'Проверка что name в ответе соответствует Elena3'):
        assert response.json()['name'] == 'Elena3', 'В ответе вернулся неверный параметр name'


@allure.title('Удаление объекта')
@allure.feature('Objects')
@allure.story('Objects manipulation')
@allure.issue('https://cs14.pikabu.ru/post_img/big/2023/11/09/6/1699523283119573488.jpg', 'ST-637')
def test_delete_object(new_object_id, start_end_test):
    with allure.step(f'Отправка запроса на удаление объекта с id {new_object_id}'):
        response = requests.delete(f'{url}/{new_object_id}')
    with allure.step('Проверка статус код = 200'):
        assert response.status_code == 201, 'Неверный статус код'
