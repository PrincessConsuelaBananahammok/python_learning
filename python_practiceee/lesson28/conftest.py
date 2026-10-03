import pytest

from python_practiceee.lesson28.homework28.pages.home_page import HomePage
from python_practiceee.lesson28.homework28.pages.registration_page import RegistrationPage
from python_practiceee.lesson28.registration_data import REGISTRATION_DATA


@pytest.fixture
def registration_page(page):
    page.goto("https://guest:welcome2qauto@qauto2.forstudy.space/")

    home_page = HomePage(page)
    home_page.sign_up_button.click()

    return RegistrationPage(page)


@pytest.fixture
def filled_registration_page(registration_page):
    registration_page.name.fill(REGISTRATION_DATA.name)
    registration_page.last_name.fill(REGISTRATION_DATA.last_name)
    registration_page.email.fill(REGISTRATION_DATA.email)
    registration_page.password.fill(REGISTRATION_DATA.password)
    registration_page.re_enter_password.fill(REGISTRATION_DATA.repeat_password)

    return registration_page