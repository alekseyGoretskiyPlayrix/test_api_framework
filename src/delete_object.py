from typing import Any

import requests

from src.create_object import CreateObject


class DeleteObject:
    response: Any

    def delete_object(self, object_id: str):
        self.response = requests.delete("API_URL_OBJECT_DELETE_WITHOUT_ID + object_id")
        return self.response
