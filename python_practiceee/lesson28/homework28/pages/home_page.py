from playwright.sync_api import Page


class HomePage:
    def __init__(self, page: Page):
        self.page = page

        self.sign_up_button = page.get_by_role("button", name="Sign up")

    def click_sign_up(self):
        self.sign_up_button.click()