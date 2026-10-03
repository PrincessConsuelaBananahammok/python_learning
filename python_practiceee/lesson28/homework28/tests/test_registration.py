from python_practiceee.lesson28.homework28.pages.garage_page import GaragePage
from python_practiceee.lesson28.registration_data import REGISTRATION_DATA



def test_registration(filled_registration_page):
    filled_registration_page.register_button.click()

    filled_registration_page.page.wait_for_url("**/panel/garage")

    garage_page = GaragePage(filled_registration_page.page)

    assert garage_page.garage_title.is_visible()