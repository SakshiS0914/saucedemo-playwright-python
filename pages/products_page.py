from playwright.sync_api import Page


class ProductsPage:

    def __init__(self, page: Page):
        self.page = page

    def verify_product(self, product_name):
        product = self.page.locator(
            ".inventory_item"
        ).filter(
            has_text=product_name
        )

        product.is_visible()

    def get_product_price(self, product_name):
        product = self.page.locator(
            ".inventory_item"
        ).filter(
            has_text=product_name
        )

        price = product.locator(
            ".inventory_item_price"
        ).text_content()

        return price

    def add_product(self, product_name):
        product = self.page.locator(
            ".inventory_item"
        ).filter(
            has_text=product_name
        )

        product.get_by_role(
            "button",
            name="Add to cart"
        ).click()

    def open_cart(self):
        self.page.locator(
            ".shopping_cart_link"
        ).click()