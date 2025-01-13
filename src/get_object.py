import requests

from config import API_BASE_URL
from src.base_object import BaseObject


class GetObject(BaseObject):

    def get_object(self, object_id: int):
        self.response = requests.get(f'{API_BASE_URL}/{object_id}')
        return self.get_response_json()
