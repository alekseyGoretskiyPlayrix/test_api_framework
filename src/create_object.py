import requests

from src.base_object import BaseObject


class CreateObject(BaseObject):

    def create_object(self, payload: dict):
        self.response = requests.post(self.base_url, json=payload)
        return self.get_response_json()

    def get_id_created_object(self):
        response_data = self.get_response_json()
        return response_data.get('id')
