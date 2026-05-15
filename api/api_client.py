import requests
from utilities.read_config import ReadConfig

BASE_URL = ReadConfig.get_api_url()

class APIClient:

    @staticmethod
    def post(endpoint, payload=None, headers=None):

        return requests.post(
            BASE_URL + endpoint,
            json=payload,
            headers=headers
        )

    @staticmethod
    def get(endpoint, headers=None):

        return requests.get(
            BASE_URL + endpoint,
            headers=headers
        )

    @staticmethod
    def put(endpoint, payload=None, headers=None):

        return requests.put(
            BASE_URL + endpoint,
            json=payload,
            headers=headers
        )

    @staticmethod
    def delete(endpoint, headers=None):

        return requests.delete(
            BASE_URL + endpoint,
            headers=headers
        )