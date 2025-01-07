from typing import Any

import requests


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
        response = requests.post("https://api.restful-api.dev/objects", json=self.payload)
