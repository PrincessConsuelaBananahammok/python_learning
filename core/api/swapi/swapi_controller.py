import requests

from core.api.basic_controller import BasicController


class SwapiController(BasicController):
    def __init__(self, url="https://swapi.info/api/"):
        self.url = url

    def get_person(self, person_id, params=None):
        url = f"{self.url}people/{person_id}"
        """
        send request to get /api/people/{person_id}
        :return:
        """

        # if page is not None:
        #     url = url + f"?page={page}"

        # return requests.get(url=url, params=None)
        return self._execute_request(method="get", url = url)

    def get_people(self, params=None):
        url = f"{self.url}people/"

        # return requests.get(url=url, params=params) - змінили бо додали Bacis_controller
        return self._execute_request(method="get", url = url, params=params)


