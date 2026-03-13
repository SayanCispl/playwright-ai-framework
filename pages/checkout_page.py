from playwright.sync_api import Page
from config.config import Config


class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.proceed_to_checkout_button = "a.btn.btn-default.check_out"

    def navigate(self):
        self.page.goto(Config.CART_URL)
        self.page.wait_for_load_state("networkidle")

    def checkout(self):
        # Verify we're on the cart page with items
        try:
            self.page.wait_for_selector(self.proceed_to_checkout_button, timeout=10000)
        except Exception as e:
            # Take a screenshot for debugging if button doesn't appear
            self.page.screenshot(path="screenshots/cart_empty_debug.png")
            raise Exception(f"Checkout button not found. Cart might be empty. Error: {e}")

        self.page.click(self.proceed_to_checkout_button)
        self.page.wait_for_load_state("networkidle")

    def is_checkout_page(self) -> bool:
        return "/checkout" in self.page.url