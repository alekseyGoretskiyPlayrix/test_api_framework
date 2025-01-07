from typing import Any

import requests

from config import API_URL_OBJECT_3


class GetObject:
    response: Any

    def get_object(self):
        self.response = requests.get(API_URL_OBJECT_3)
        return self.response.json()
