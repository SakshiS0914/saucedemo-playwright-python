from playwright.sync_api import Page, expect


class CheckoutPage:

    def __init__(self, page: Page):
        self.page = page

    def fill_customer_details(
        self,
        first_name,
        last_name,
        postal_code
    ):
        self.page.get_by_placeholder(
            "First Name"
        ).fill(first_name)

        self.page.get_by_placeholder(
            "Last Name"
        ).fill(last_name)

        self.page.get_by_placeholder(
            "Zip/Postal Code"
        ).fill(postal_code)

    def continue_checkout(self):
        self.page.get_by_role(
            "button",
            name="Continue"
        ).click()

    def finish_order(self):
        self.page.get_by_role(
            "button",
            name="Finish"
        ).click()

    def verify_order_completion(self):
        expect(
            self.page.get_by_text(
                "Thank you for your order!",
                exact=True
            )
        ).to_be_visible()