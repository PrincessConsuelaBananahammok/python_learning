import unittest

from core.api.swapi.swapi_controller import SwapiController

swapi_controller = SwapiController()

class TestPerson(unittest.TestCase):

    # def test_get_person(self):
    #     response = requests.get(url="https://swapi.info/api/people/1") - замінюєм урлу
    #     self.assertEqual(200, response.status_code)

    # def test_get_person(self):
    #     response = requests.get(url=f"{SwapiController().url}people/1") - person id в окрему змінну
    #     self.assertEqual(200, response.status_code)

    # def test_get_person(self):
    #     person_id = 1
    #     response = requests.get(url=f"{SwapiController().url}people/{person_id}") -
    #     - прописуємо ендп як метод в swapi_controller, тож це можна поміняти
    #     self.assertEqual(200, response.status_code)

    def test_get_person(self):
        person_id = 1
        response = swapi_controller.get_person(person_id)
        self.assertEqual(200, response.status_code)

    # def test_get_people(self):
    #     response = requests.get(url=f"{SwapiController().url}") -
    # - - прописуємо ендп як метод в swapi_controller, тож це можна поміняти
    # -тому тут ми не будем викликати запит, ми будем викликати метод шо цей запит зробить
    #     self.assertEqual(200, response.status_code)

    def test_get_people(self):
        response = swapi_controller.get_people()
        self.assertEqual(200, response.status_code)
