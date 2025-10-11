import pytest

def test_get_objects(get_objects_endpoint):
        get_objects_endpoint.get_objects()
        get_objects_endpoint.check_status_code_is_200()

def test_get_object(get_object_endpoint):
    get_object_endpoint.get_object(1)
    get_object_endpoint.check_status_code_is_200()

TEST_DATA = [
    {"name": 'Elena', "data": {"level": 1, "group": 357}},
    {"name": 'Olga', "data": {"level": 14, "group": 37}},
    {"name": 'Nikolay', "data": {"level": 13, "group": 3}},
    {"name": 'Oleg', "data": {"level": 13, "group": 234}},
    {"name": 'Anastasya', "data": {"level": 8, "group": 78}}
]

@pytest.mark.parametrize('data', TEST_DATA)
def test_post_object(create_object_endpoint, data):
    create_object_endpoint.create_new_object(payload=data)
    create_object_endpoint.check_status_code_is_200()
    create_object_endpoint.check_response_name_is_correspond(data['name'])


def test_put_object(put_object_endpoint):
    body = {
        "name": "Elena2",
        "data": {
            "level": 2,
            "group": 2
        }
    }
    put_object_endpoint.put_object(1, payload=body)
    put_object_endpoint.check_status_code_is_200()
    put_object_endpoint.check_response_name_is_correspond(body['name'])


def test_patch_object(patch_object_endpoint):
    body = {
        "name": "Elena3"
    }
    object_id = 1
    patch_object_endpoint.patch_object(object_id=object_id, payload=body)
    patch_object_endpoint.check_response_name_is_correspond(body['name'])
    patch_object_endpoint.check_status_code_is_200()


def test_delete_object(delete_object_endpoint):
    delete_object_endpoint.delete_object(1)
    delete_object_endpoint.check_status_code_is_403()
