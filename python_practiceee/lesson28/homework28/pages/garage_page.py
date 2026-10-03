from playwright.sync_api import Page


class GaragePage:
    def __init__(self, page: Page):
        self.page = page

        self.garage_title = page.locator("h1", has_text="Garage")