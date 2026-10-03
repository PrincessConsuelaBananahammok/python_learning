import allure
import pytest

from python_practiceee.lesson28.homework28.pages.garage_page import GaragePage
from python_practiceee.lesson28.registration_data import REGISTRATION_DATA

@allure.epic("UI")
@allure.feature("Registration")
@allure.story("User registration")
@allure.title("Check successful user registration")
@allure.description("This test checks that a user can successfully register and open the Garage page")
@allure.tag("positive", "registration")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.ui
def test_registration(registration_page):
    registration_page.fill_registration_form(REGISTRATION_DATA)
    registration_page.click_register()

    garage_page = GaragePage(registration_page.page)

    garage_page.wait_for_garage_page()

    assert garage_page.is_garage_opened()

