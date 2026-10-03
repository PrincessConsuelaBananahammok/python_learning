import unittest
import time

import allure

from core.api.gorest.gorest_controller import GorestController

gorest_controller = GorestController()

class TestUserCreate(unittest.TestCase):

    @allure.epic("API")
    @allure.feature("Gorest feature")
    @allure.story("Gorest story")
    def test_create_user(self):


        user_data = {"name": "Tenali Ramakrishna", "email": f"tenali@{time.time()}example.com",
                     "gender": "male", "status": "active"}

        response = gorest_controller.create_user(user_data)

        self.assertEqual(201, response.status_code)



