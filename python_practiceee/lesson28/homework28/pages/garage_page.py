import allure
from playwright.sync_api import Page


class GaragePage:
    def __init__(self, page: Page):
        self.page = page

        self.garage_title = page.locator("h1", has_text="Garage")

    @allure.step("Check that Garage page is opened")
    def is_garage_opened(self):
        return self.garage_title.is_visible()

    @allure.step("Wait for Garage page")
    def wait_for_garage_page(self):
        self.page.wait_for_url("**/panel/garage")