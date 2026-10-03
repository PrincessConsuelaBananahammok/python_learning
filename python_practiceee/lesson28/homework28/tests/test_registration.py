from python_practiceee.lesson28.homework28.pages.garage_page import GaragePage
from python_practiceee.lesson28.registration_data import REGISTRATION_DATA



def test_registration(registration_page):
    registration_page.fill_registration_form(REGISTRATION_DATA)
    registration_page.click_register()

    registration_page.page.wait_for_url("**/panel/garage")

    garage_page = GaragePage(registration_page.page)

    assert garage_page.is_garage_opened()

