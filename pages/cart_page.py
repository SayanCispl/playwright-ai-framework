from playwright.sync_api import Page
from config.config import Config


class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.add_to_cart_button = "(//a[contains(text(),'Add to cart')])[1]"
        self.view_cart_button = "a[href='/view_cart']"

    def navigate(self):
        self.page.goto(Config.SHOP_URL)

    def add_item_to_cart(self):
        # Locate the button
        add_to_cart = self.page.locator(self.add_to_cart_button)

        # Hover to reveal the overlay (triggers the hover effect)
        add_to_cart.hover()

        # Wait for hover animation to complete (300ms is usually enough)
        self.page.wait_for_timeout(300)

        # Now click the button
        add_to_cart.click()

        # Rest of the flow
        self.page.wait_for_selector(self.view_cart_button)
        self.page.click(self.view_cart_button)

    def is_cart_page(self) -> bool:
        return self.page.url.startswith(Config.CART_URL)