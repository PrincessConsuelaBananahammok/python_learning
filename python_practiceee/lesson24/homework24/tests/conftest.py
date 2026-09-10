import pytest
import requests
from requests.auth import HTTPBasicAuth
import logging.config
import os

from constants import BASE_PROJECT_PATH


config_file_path = os.path.join(BASE_PROJECT_PATH, 'logging_config.ini')
logging.config.fileConfig(config_file_path)

logger = logging.getLogger("testSearchLogger")


BASE_URL = "http://127.0.0.1:8080"
USERNAME = "test_user"
PASSWORD = "test_pass"


@pytest.fixture(scope="class")
def auth_session():
    session = requests.Session()

    response = session.post(
        url=f"{BASE_URL}/auth",
        auth=HTTPBasicAuth(USERNAME, PASSWORD),
        json={}
    )

    logger.info(f"Auth status code: {response.status_code}")
    logger.info("Auth successful, access token received")

    access_token = response.json()["access_token"]

    session.headers.update({
        "Authorization": f"Bearer {access_token}"
    })

    return session
