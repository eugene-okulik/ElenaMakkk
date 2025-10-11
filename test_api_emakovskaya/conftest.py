import pytest
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
