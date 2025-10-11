import requests
import allure
from test_api_emakovskaya.endpoints.endpoint import Endpoint


class UpdateObject(Endpoint):
    allure.step('Update an object (Put)')

    def put_object(self, object_id, payload):
        self.response = requests.put(
            f'{self.url}/{object_id}',
            json=payload
        )
        self.response_in_json = self.response.json()
        return self.response
