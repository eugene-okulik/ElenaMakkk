import allure


class Endpoint:
    url = 'http://objapi.course.qa-practice.com/object'
    response = None
    response_in_json = None

    @allure.step('check that name in response corresponds to name from request')
    def check_response_name_is_correspond(self, name):
        assert self.response_in_json['name'] == name

    @allure.step('check response status code is 200')
    def check_status_code_is_200(self):
        assert self.response.status_code == 200

    @allure.step('check response status code is 403')
    def check_status_code_is_403(self):
        assert self.response.status_code == 403
