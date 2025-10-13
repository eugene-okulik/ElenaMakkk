import requests
import allure
from test_api_emakovskaya.endpoints.endpoint import Endpoint


class GetObjects(Endpoint):
    allure.step('get objects')

    def get_objects(self, url=None):
        url = url if url else self.url
        self.response = requests.get(url=url)
        self.response_in_json = self.response.json()
        return self.response
