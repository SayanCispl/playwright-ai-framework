from playwright.sync_api import Page
from config.config import Config


class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.add_to_cart_button = "(//a[contains(text(),'Add to cart')])[1]"
        self.view_cart_button = "a[href='/view_cart']"
        self.continue_shopping_button = "text='Continue Shopping'"
        # Modal that appears after adding to cart
        self.cart_modal = "#cartModal"

    def navigate(self):
        self.page.goto(Config.SHOP_URL)
        # Wait for products to load
        self.page.wait_for_load_state("networkidle")

    def add_item_to_cart(self):
        # Scroll to the first product to ensure it's in view
        self.page.locator(self.add_to_cart_button).scroll_into_view_if_needed()

        # Wait a moment for any animations
        self.page.wait_for_timeout(500)

        # Use JavaScript click as a more reliable alternative
        self.page.locator(self.add_to_cart_button).evaluate("element => element.click()")

        # Wait for the modal to confirm item was added
        self.page.wait_for_selector(self.cart_modal, state="visible", timeout=10000)

        # Click "View Cart" from the modal
        self.page.click(self.view_cart_button)

        # Wait for cart page to load
        self.page.wait_for_url("**/view_cart")

    def is_cart_page(self) -> bool:
        return self.page.url.startswith(Config.CART_URL)