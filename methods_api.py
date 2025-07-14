import requests
from data import Urls


class API:

    @staticmethod
    def create_user(payload):
        response = requests.post(Urls.REGISTRATION_URL, data=payload)
        return response.json()

    @staticmethod
    def delete_user(headers):
        response = requests.delete(Urls.DELETE_USER_URL, headers=headers)
        return response.json()
