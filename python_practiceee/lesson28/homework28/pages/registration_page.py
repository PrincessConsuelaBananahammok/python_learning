import allure
from playwright.sync_api import Page


class RegistrationPage:
    def __init__(self, page: Page):
        self.page = page

        self.name = page.locator("#signupName")
        self.last_name = page.locator("#signupLastName")
        self.email = page.locator("#signupEmail")
        self.password = page.locator("#signupPassword")
        self.re_enter_password = page.locator("#signupRepeatPassword")
        self.register_button = page.get_by_role("button", name="Register")

    @allure.step("Fill registration form")
    def fill_registration_form(self, data):
        self.name.fill(data.name)
        self.last_name.fill(data.last_name)
        self.email.fill(data.email)
        self.password.fill(data.password)
        self.re_enter_password.fill(data.repeat_password)

    @allure.step("Click Register button")
    def click_register(self):
        self.register_button.click()