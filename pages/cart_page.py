from playwright.sync_api import Page
from config.config import Config


class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.add_to_cart_button = "(//a[contains(text(),'Add to cart')])[1]"
        self.view_cart_button = "a[href='/view_cart']"
        # Add selector for the product container
        self.first_product = ".product-image-wrapper:first-of-type"  # or ".single-products:first-of-type"

    def navigate(self):
        self.page.goto(Config.SHOP_URL)

    def add_item_to_cart(self):
        # Hover the product container (not the button) to trigger the overlay
        self.page.hover(self.first_product)

        # Wait for the overlay animation
        self.page.wait_for_timeout(500)

        # Now click with force to bypass any remaining blocking
        self.page.locator(self.add_to_cart_button).click(force=True)

        # Rest of the flow
        self.page.wait_for_selector(self.view_cart_button)
        self.page.click(self.view_cart_button)

    def is_cart_page(self) -> bool:
        return self.page.url.startswith(Config.CART_URL)