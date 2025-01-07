from typing import Any

import requests

from config import PAYLOAD_OBJECT_CREATION, API_URL_OBJECT_CREATION


class CreateObject:
    response: Any

    def create_object(self):
        self.response = requests.post(API_URL_OBJECT_CREATION, json=PAYLOAD_OBJECT_CREATION)
        return self.response.json()
