from typing import Any

import requests

from config import PAYLOAD_OBJECT_UPDATE, API_URL_OBJECT_PUT_7


class UpdateObject:
    response: Any

    def update_object(self):
        self.response = requests.put(API_URL_OBJECT_PUT_7, json=PAYLOAD_OBJECT_UPDATE)
        return self.response.json()
