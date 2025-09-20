import requests

url = 'http://objapi.course.qa-practice.com/object'
body = {
    "name": "Elena",
    "data": {
        "level": 1,
        "group": 357
    }
}


def post_new_object(req_body):
    response = requests.post(url, json=req_body).json()
    return response['id']


def clear(object_id):
    requests.delete(f'{url}/{object_id}')


# Получение списка всех объектов
def get_objects():
    response = requests.get(url)
    assert response.status_code == 200, 'status code is not correct'


# Получение одного объекта по id
def get_object(object_id):
    response = requests.get(f'{url}/{object_id}')
    assert response.json()['id'] == object_id


# Добавление нового объекта
def post_object(req_body):
    response = requests.post(url, json=req_body)
    assert response.json()['name'] == 'Elena'
    object_id = response.json()['id']
    clear(object_id)


# Изменение существующего объекта (put)
def put_object(req_body):
    object_id = post_new_object(body)
    response = requests.put(f'{url}/{object_id}', json=req_body)
    print(response.json())
    print(response.status_code)
    assert response.status_code == 200, 'Неверный статус код'
    assert response.json()['name'] == 'Елена', 'В ответе вернулся неверный параметр name'
    clear(object_id)


# Изменение существующего объекта (patch)
def patch_object(req_body):
    object_id = post_new_object(body)
    response = requests.patch(f'{url}/{object_id}', json=req_body)
    assert response.status_code == 200, 'Неверный статус код'
    assert response.json()['name'] == 'Елена', 'В ответе вернулся неверный параметр name'


# Удаление объекта
def delete_object():
    object_id = post_new_object(body)
    response = requests.delete(f'{url}/{object_id}')
    print(response.status_code)
    assert response.status_code == 201, 'Неверный статус код'


get_objects()
get_object(1)
post_object(body)
put_object(body)
patch_object(body)
delete_object()
