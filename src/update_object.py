from typing import Any

import requests

from config import PAYLOAD_OBJECT_UPDATE, API_URL_OBJECT_PUT


class UpdateObject:
    response: Any

    def update_object(self):
        response = requests.put(f'{API_URL_OBJECT_PUT}{'ff808181932badb601945f80c66522b6'}',
                                json=PAYLOAD_OBJECT_UPDATE)
        return response.json()
