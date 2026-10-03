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