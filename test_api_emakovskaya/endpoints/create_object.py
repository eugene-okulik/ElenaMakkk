import requests
import allure
from test_api_emakovskaya.endpoints.endpoint import Endpoint


class Create_object(Endpoint):

    @allure.step('Create new object')
    def create_new_object(self, payload):
        self.response = requests.post(
            self.url,
            json=payload
        )
        self.response_in_json = self.response.json()
        return self.response

    @allure.step('Create new object')
    def new_object_id(self):
        body = {
            "name": "Elena",
            "data": {
                "level": 1,
                "group": 357
            }
        }
        self.response = requests.post(self.url, json=body).json()
        object_id = self.response['id']
        yield object_id
        requests.delete(f'{self.url}/{object_id}')
