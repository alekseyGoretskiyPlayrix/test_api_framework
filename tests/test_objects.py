import pytest

from config import *
from src.create_object import CreateObject
from src.delete_object import DeleteObject
from src.get_object import GetObject
from src.update_object import UpdateObject


@pytest.fixture
def create_default_object():
    default_object = CreateObject()
    default_object.create_object(PAYLOAD_OBJECT_CREATION)
    return default_object


class TestObjects:

    def test_create_object(self, create_default_object):
        object = create_default_object

        assert object.response.status_code == STATUS_CODE_200, "Object was not created successfully"

        assert object.get_response_json().get('name') == PAYLOAD_OBJECT_CREATION[
            'name'], "Name does not match the expected value"
        assert object.get_response_json().get('data', {}).get('year') == PAYLOAD_OBJECT_CREATION['data'][
            'year'], "Year does not match the expected value"
        assert object.get_response_json().get('data', {}).get('price') == PAYLOAD_OBJECT_CREATION['data'][
            'price'], "Price does not match the expected value"
        assert object.get_response_json().get('data', {}).get('CPU model') == PAYLOAD_OBJECT_CREATION['data'][
            'CPU model'], "CPU model does not match the expected value"
        assert object.get_response_json().get('data', {}).get('Hard disk size') == PAYLOAD_OBJECT_CREATION['data'][
            'Hard disk size'], "Hard disk size does not match the expected value"

    def test_get_object(self):
        object = GetObject().get_object(3)
        assert object['id'] == PAYLOAD_GET_OBJECT_3['id']

    # тут еще добавить остальные поля + статус код

    def test_update_object(self):
        object = UpdateObject()
        response = object.update_object()
        assert response['name'] == PAYLOAD_OBJECT_UPDATE['name']

    def test_delete_object(self, create_default_object):
        object_id = 'ff808181932badb601945f80c66522b6'
        object = DeleteObject()
        response = object.delete_object(object_id)
        assert response.status_code == 404
