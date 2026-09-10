from python_practiceee.lesson24.homework24.tests.conftest import BASE_URL
from python_practiceee.lesson24.homework24.tests.conftest import logger


class TestCars:

    def test_auth(self, auth_session):
        response = auth_session.get(f"{BASE_URL}/cars")



        logger.info(f"Cars status code: {response.status_code}")
        logger.info(f"Cars response: {response.json()}")

        assert response.status_code == 200

