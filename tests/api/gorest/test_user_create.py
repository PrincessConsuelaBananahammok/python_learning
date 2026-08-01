import unittest
import time

from core.api.gorest.gorest_controller import GorestController

gorest_controller = GorestController()

class TestUserCreate(unittest.TestCase):

    def test_create_user(self):
        user_data = { "name": "Tenali Ramakrishna", "email": "tenali3333@example.com",
                       "gender": "male", "status": "active" }

        response = gorest_controller.create_user(user_data)
        pass

        self.assertEqual(201, response.status_code)



