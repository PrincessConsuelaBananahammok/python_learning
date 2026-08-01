import requests

from core.api.basic_controller import BasicController


class GorestController(BasicController):
    def __init__(self, url="https://gorest.co.in/public/v2/"):
        self.url = url
        self.token = self.get_token

    def get_token(self):
        return "e6a7ee9104a0237687d91292fb61d7c2c5e371f48ee894a31eb1be5e76db4529"

    def get_user(self, person_id, params=None):
        url = f"{self.url}people/{person_id}"
        """
        send request to get /api/people/{person_id}
        :return:
        """

        # if page is not None:
        #     url = url + f"?page={page}"

        # return requests.get(url=url, params=None)
        return self._execute_request(method="get", url=url, params=params)

    def get_users(self, params=None):
        url = f"{self.url}people/"
        # return requests.get(url=url, params=params)
        return self._execute_request(method="get", params=params)

    def create_user(self, data):
        url = f"{self.url}users"
        # return requests.post(url=url, data=data, headers={"Authorization": f"Bearer {self.get_token()}"})
        return requests.post(url=url, data=data, headers={"Authorization": f"Bearer {self.get_token()}"})



