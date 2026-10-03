import time

import allure
from playwright.sync_api import sync_playwright, expect

import pytest

from core.data.login_data import INVALID_LOGIN_DATA
from core.data.login_data import STANDARD_LOGIN
from core.pages.login_page import LoginPage


# def test_login_positive(playwright):
#     # with sync_playwright() as playwright:
#         browser = playwright.chromium.launch(
#             headless=False,
#             args=["--start-maximized"]
#         )
#         context = browser.new_context(
#             no_viewport=True
#         )
#         page = browser.new_page()
#         page.goto("https://www.saucedemo.com")
#         # page.wait_for_timeout(3000)
#         username_locator = page.locator("//input[@placeholder='Username']")
#         username_locator.fill("standard_user")
#         # page.wait_for_timeout(3000)
#         pass_locator = page.locator("#password")
#         pass_locator.fill("secret_sauce")
#         # page.wait_for_timeout(3000)
#         page.get_by_role("button", name="Login").click()
#         # page.wait_for_timeout(3000)
#         logo_locator = page.locator(".app_logo")
#         expect(logo_locator).to_be_visible()
#         expect(page).to_have_title("Swag Labs")
#         expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
#         # browser.close()


#2
# @pytest.mark.ui
# def test_login_positive_second(login_page):
    # with sync_playwright() as playwright:
    #     browser = playwright.chromium.launch(
    #         headless=False,
    #         args=["--start-maximized"]
    #     )
    #     context = browser.new_context(
    #         no_viewport=True
    #     )
    #     page = browser.new_page()
    #     page.goto("https://www.saucedemo.com")
    #     # page.wait_for_timeout(3000)
    #     username_locator = page.locator("//input[@placeholder='Username']")
    #     username_locator.fill("standard_user")
    #     # page.wait_for_timeout(3000)
    #     pass_locator = page.locator("#password")
    #     pass_locator.fill("secret_sauce")
    #     # page.wait_for_timeout(3000)
    #     page.get_by_role("button", name="Login").click()
    #     # page.wait_for_timeout(3000)


#         expect(page).to_have_title("Swag Labs")
        # expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
        # browser.close()

@allure.epic("UI")
@allure.feature("SauceDemo")
@allure.story("Test login")
@pytest.mark.ui
def test_login_positive_second(login_page):
    login_page.open()
    inventory_page = login_page.login_valid_user(STANDARD_LOGIN.username, STANDARD_LOGIN.password)
    inventory_page.is_displayed()
    inventory_page.img_loaded()

@allure.epic("UI")
@allure.feature("SauceDemo")
@allure.story("Test login")
@pytest.mark.ui
def test_login_click_enter(login_page):
    login_page.open()
    inventory_page = login_page.login_via_enter(STANDARD_LOGIN.username, STANDARD_LOGIN.password)
    inventory_page.is_displayed()
    inventory_page.img_loaded()


@allure.epic("UI")
@allure.feature("SauceDemo")
@allure.story("Test login")
@pytest.mark.parametrize(
    "test_data",
    INVALID_LOGIN_DATA
    # [
    #     ("standard_user", "wrong_pass", "Epic sadface: Username and password do not match any user in this service"),
    #     ("", "wrong_pass", "Epic sadface: Username is required"),
    #     ("locked_out_user", "secret_sauce", "Epic sadface: Sorry, this user has been locked out."),
    # ]
)
def test_login_wrong_password(login_page, test_data):
    login_page.open()
    # login_page.do_invalid_login(test_data.username, test_data.password)
    login_page.do_invalid_login(test_data.username, test_data.password)
    # assert login_page.get_error_message() == test_data.expected_error
    assert login_page.get_error_message() == test_data.expected_error
    # (expect(login_page.get_error_element()).
    #  to_have_text("Epic sadface: Username and password do not match any user in this service"))
    # (expect(login_page.get_error_element())
    #  .to_contain_text("Epic sadface"))

