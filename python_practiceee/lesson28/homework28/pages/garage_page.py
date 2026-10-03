from playwright.sync_api import Page


class GaragePage:
    def __init__(self, page: Page):
        self.page = page

        self.garage_title = page.locator("h1", has_text="Garage")

    def is_garage_opened(self):
        return self.garage_title.is_visible()