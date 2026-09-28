from playwright.sync_api import expect

from pages.login_page import LoginPage


def test_valid_login(page):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    expect(
        page.get_by_text(
            "Products",
            exact=True
        )
    ).to_be_visible()


def test_invalid_username(page):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login(
        "invalid_user",
        "secret_sauce"
    )

    expect(
        page.get_by_text(
            "Epic sadface: Username and password do not match any user in this service"
        )
    ).to_be_visible()


def test_invalid_password(page):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login(
        "standard_user",
        "invalid_password"
    )

    expect(
        page.get_by_text(
            "Epic sadface: Username and password do not match any user in this service"
        )
    ).to_be_visible()