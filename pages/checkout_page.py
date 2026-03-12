from playwright.sync_api import Page
from config.config import Config

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.proceed_to_checkout_button = "a.btn.btn-default.check_out"

    def navigate(self):
        self.page.goto(Config.CART_URL)

    def checkout(self):
        self.page.wait_for_selector(self.proceed_to_checkout_button)
        self.page.click(self.proceed_to_checkout_button)

    def is_checkout_page(self) -> bool:
        return "/checkout" in self.page.url
