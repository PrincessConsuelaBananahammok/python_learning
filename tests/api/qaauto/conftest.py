from pytest import fixture

from core.api.qaauto.qa_auto_controller import QAAUTOController
from settings import settings



@fixture(scope="session")
def qa_auto_controller():
    qa_auto_controller = QAAUTOController()
    yield qa_auto_controller

@fixture(scope="session", autouse=True)#кожен раз коли буде запускатись сесія тестів, то запусти ось цю фіксутуру
#в не залежності від того ця фікстура прокинута тестом чи ні
def login(qa_auto_controller):
    body = {
        "email": settings.USER_EMAIL,
        "password": settings.USER_PASS,
        "remember": False
    }
    qa_auto_controller.login(json=body)
    print("Login user")
    yield
    print("Test finished")
