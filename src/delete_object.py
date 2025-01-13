from typing import Any

import requests

from config import API_URL_OBJECT_DELETE_WITHOUT_ID


class DeleteObject:
    response: Any

    def delete_object(self, object_id: str):
        self.response = requests.delete(f"{API_URL_OBJECT_DELETE_WITHOUT_ID}{object_id}")
        return self.response

object = DeleteObject()
x = object.delete_object('ff808181932badb601945f80c66522b6')
print(x.status_code)