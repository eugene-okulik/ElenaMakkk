import requests
import allure
from test_api_emakovskaya.endpoints.endpoint import Endpoint


class GetObject(Endpoint):
    allure.step('get object')
    def get_object(self, object_id, url=None):
        url = url if url else self.url
        self.response=requests.get(url=f'{url}/{object_id}')
        self.response_in_json = self.response.json()
        return self.response
