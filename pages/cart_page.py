from playwright.sync_api import Page, expect


class CartPage:

    def __init__(self, page: Page):
        self.page = page

    def verify_product(self, product_name):
        expect(
            self.page.get_by_text(
                product_name,
                exact=True
            )
        ).to_be_visible()

    def proceed_to_checkout(self):
        self.page.get_by_role(
            "button",
            name="Checkout"
        ).click()