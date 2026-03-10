from playwright.sync_api import Page
from config.config import Config

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        # Example selectors (adjust after inspecting site)
        self.proceed_to_checkout_button = "a[href='/checkout']"
        self.place_order_button = "button[data-qa='place-order']"
        self.confirmation_message = "h2"  # adjust to actual confirmation element

    def navigate(self):
        self.page.goto(Config.CART_URL)

    def checkout(self):
        # Proceed to checkout
        self.page.click(self.proceed_to_checkout_button)
        # Place order (if site requires)
        self.page.click(self.place_order_button)

    def is_order_confirmed(self) -> bool:
        # Check for confirmation message or URL
        return "order" in self.page.url or "success" in self.page.inner_text(self.confirmation_message).lower()
