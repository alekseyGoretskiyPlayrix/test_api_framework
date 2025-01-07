from typing import Any

import requests

from config import PAYLOAD_OBJECT_CREATION, API_URL_OBJECT_CREATION


class CreateObject:
    response: Any

    payload = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }

    def create_object(self):
        self.response = requests.post(API_URL_OBJECT_CREATION, json=PAYLOAD_OBJECT_CREATION)
        return self.response.json()
