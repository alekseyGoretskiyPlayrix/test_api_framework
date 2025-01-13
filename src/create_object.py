from http.client import responses
from typing import Any

import requests

from config import PAYLOAD_OBJECT_CREATION, API_URL_OBJECT_CREATION


class CreateObject:
    response: Any

    def create_object(self):
        self.response = requests.post(API_URL_OBJECT_CREATION, json=PAYLOAD_OBJECT_CREATION)
        return self.response.json()

    def get_id_created_object(self):
        response_created_object = self.response.json()
        return response_created_object['id']

object = CreateObject()
response = object.create_object()
print(response)

id = object.get_id_created_object()
print(id)