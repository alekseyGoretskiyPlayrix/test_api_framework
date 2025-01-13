from typing import Any

import requests

from config import PAYLOAD_OBJECT_UPDATE, API_URL_OBJECT_PUT


class UpdateObject:
    response: Any

    #переписать так что в параметры передавался уже созданный объект


    def update_object(self, object_id):
        self.response = requests.put(f'{API_URL_OBJECT_PUT}{object_id}', json=PAYLOAD_OBJECT_UPDATE)
        return self.response.json()
