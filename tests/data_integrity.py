from playwright.sync_api import expect

from pages.login_page import LoginPage
from pages.products_page import ProductsPage


def test_product_price(page):

    login_page = LoginPage(page)
    products_page = ProductsPage(page)

    login_page.open()

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    product_name = "Sauce Labs Backpack"

    product_price = products_page.get_product_price(
        product_name
    )

    print(
        "Product price:",
        product_price
    )

    products_page.add_product(
        product_name
    )

    products_page.open_cart()

    page.get_by_role(
        "button",
        name="Checkout"
    ).click()

    page.get_by_placeholder(
        "First Name"
    ).fill("John")

    page.get_by_placeholder(
        "Last Name"
    ).fill("Doe")

    page.get_by_placeholder(
        "Zip/Postal Code"
    ).fill("12345")

    page.get_by_role(
        "button",
        name="Continue"
    ).click()

    checkout_price = page.locator(
        ".inventory_item_price"
    ).text_content()

    assert checkout_price.strip() == product_price.strip()


def test_checkout_calculation(page):

    login_page = LoginPage(page)
    products_page = ProductsPage(page)

    login_page.open()

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    products_page.add_product(
        "Sauce Labs Backpack"
    )

    products_page.open_cart()

    page.get_by_role(
        "button",
        name="Checkout"
    ).click()

    page.get_by_placeholder(
        "First Name"
    ).fill("John")

    page.get_by_placeholder(
        "Last Name"
    ).fill("Doe")

    page.get_by_placeholder(
        "Zip/Postal Code"
    ).fill("12345")

    page.get_by_role(
        "button",
        name="Continue"
    ).click()

    # Get Item Total
    item_total_text = page.locator(
        '[data-test="subtotal-label"]'
    ).text_content()

    # Get Tax
    tax_text = page.locator(
        '[data-test="tax-label"]'
    ).text_content()

    # Get Final Total
    total_text = page.locator(
        '[data-test="total-label"]'
    ).text_content()

    # Convert Item Total to number
    item_total = float(
        item_total_text.replace(
            "Item total: $",
            ""
        )
    )

    # Convert Tax to number
    tax = float(
        tax_text.replace(
            "Tax: $",
            ""
        )
    )

    # Convert Total to number
    total = float(
        total_text.replace(
            "Total: $",
            ""
        )
    )

    # Verify calculation
    assert round(item_total + tax, 2) == total