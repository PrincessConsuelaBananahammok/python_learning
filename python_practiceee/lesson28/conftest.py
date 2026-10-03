import pytest

from python_practiceee.lesson28.homework28.pages.home_page import HomePage
from python_practiceee.lesson28.homework28.pages.registration_page import RegistrationPage


@pytest.fixture
def registration_page(page):
    page.goto("https://guest:welcome2qauto@qauto2.forstudy.space/")

    home_page = HomePage(page)
    home_page.click_sign_up()

    return RegistrationPage(page)



