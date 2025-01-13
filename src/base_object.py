from typing import Any

from config import API_BASE_URL


class BaseObject:
    base_url: str
    response: Any

    def __init__(self):
        self.base_url = API_BASE_URL

    def get_response_json(self):
        try:
            return self.response.json()
        except ValueError:
            raise ValueError("The requested URL didn't return JSON")
