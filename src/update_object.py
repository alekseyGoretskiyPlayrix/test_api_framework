import requests

from config import PAYLOAD_OBJECT_UPDATE, API_URL_OBJECT_PUT
from src.base_object import BaseObject


class UpdateObject(BaseObject):

    def update_object(self, object_id: str):
        self. response = requests.put(f'{API_URL_OBJECT_PUT}{'object_id'}',
                                json=PAYLOAD_OBJECT_UPDATE)
        return self.response.json()
