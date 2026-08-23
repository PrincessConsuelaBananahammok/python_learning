from sqlalchemy.testing import fixture

from core.api.qaauto.qa_auto_controller import QAAUTOController
from settings import settings


qaauto_controller = QAAUTOController()

@fixture
def login():
    body = {
        "email": settings.USER_EMAIL,
        "password": settings.USER_PASS,
        "remember": False
    }
    qaauto_controller.login(json=body)


def test_get_current_positive(login):
    response_current = qaauto_controller.get_current()
    assert response_current.status_code == 200
    assert response_current.json()["status"] == "ok"

def test_get_current_negative(login):
    response_current = qaauto_controller.get_current(use_cookies=False)
    assert response_current.status_code == 401
    assert response_current.json()["status"] == "error"
