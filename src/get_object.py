from typing import Any

import requests

from config import API_URL_OBJECT_GET


class GetObject:
    response: Any

    def get_object(self, object_id):
        self.response = requests.get(f'{API_URL_OBJECT_GET}{object_id}')
        return self.response.json()
