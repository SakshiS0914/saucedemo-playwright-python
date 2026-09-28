# import pytest
# from playwright.sync_api import sync_playwright

# @pytest.fixture(scope="session")
# def browser():
#    with sync_playwright() as p:
#        browser = p.chromium.launch(headless=False)
#        yield browser
#        browser.close()

# @pytest.fixture
# def page(browser):
#    page = browser.new_page()
#    yield page
#    page.close()
import pytest


@pytest.fixture
def logged_in_page(page):
    from pages.login_page import LoginPage

    login_page = LoginPage(page)

    login_page.open()
    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    return page