from locust import task, HttpUser
import random


class ObjectTest(HttpUser):
    object_id = None

    @task(3)
    def get_objects(self):
        self.client.get(
            'object'
        )

    @task(8)
    def get_object(self):
        self.client.get(
            f'object/{random.choice([1, 571, 572, 580, 585, 703, 704, 705])}'
        )

    @task(2)
    def post_object(self):
        response = self.client.post(
            'object',
            json={'name': 'Elena', 'data': {'group': 11, 'level': 3}}
        )
        self.object_id = response.json()['id']

    @task(1)
    def put_object(self):
        self.client.put(
            f'object/{self.object_id}',
            json={'name': 'Elena', 'data': {'group': 11, 'level': 3}}
        )

    @task(1)
    def delete_object(self):
        self.client.delete(
            f'object/{self.object_id}'
        )
