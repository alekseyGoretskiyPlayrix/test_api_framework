from config import PAYLOAD_OBJECT_CREATION, PAYLOAD_GET_OBJECT_3
from src.create_object import CreateObject
from src.get_object import GetObject
from src.update_object import UpdateObject


class TestObjects:

    def test_create_object(self):
        object = CreateObject().create_object()
        assert object['name'] == PAYLOAD_OBJECT_CREATION['name']
        # тут еще добавить остальные поля + статус код

    def test_get_object(self):
        object = GetObject().get_object(3)
        assert object['id'] == PAYLOAD_GET_OBJECT_3['id']
        # тут еще добавить остальные поля + статус код

    # переписать после того будет поправлен класс update object
    def test_update_object(self):
        object = CreateObject()
        object.create_object()
        object_id = object.get_id_created_object()

        updated_object = UpdateObject()
        updated_object.update_object(object_id)
        assert object_id == updated_object['id']

