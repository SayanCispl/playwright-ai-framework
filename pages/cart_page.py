from playwright.sync_api import Page
from config.config import Config


class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.add_to_cart_button = "(//a[contains(text(),'Add to cart')])[1]"
        self.view_cart_in_modal = "#cartModal a[href='/view_cart']"
        self.cart_modal = "#cartModal"

    def navigate(self):
        self.page.goto(Config.SHOP_URL)
        self.page.wait_for_load_state("networkidle")

    def add_item_to_cart(self):
        # Scroll to the first product
        self.page.locator(self.add_to_cart_button).scroll_into_view_if_needed()
        self.page.wait_for_timeout(500)

        # Use JavaScript click to bypass overlay blocking
        self.page.locator(self.add_to_cart_button).evaluate("element => element.click()")

        # Wait for modal to appear
        self.page.wait_for_selector(self.cart_modal, state="visible", timeout=10000)

        # Click the "View Cart" button inside the modal
        self.page.click(self.view_cart_in_modal)

        # Instead of strict URL wait, wait for cart page elements to load
        # This is more reliable across different browsers
        self.page.wait_for_load_state("networkidle", timeout=10000)

        # Verify we're on the cart page
        try:
            self.page.wait_for_selector(".cart_info", timeout=5000)
        except:
            # Fallback: if cart_info doesn't exist, just check URL contains 'cart'
            assert "cart" in self.page.url.lower(), f"Not on cart page. Current URL: {self.page.url}"

    def is_cart_page(self) -> bool:
        return self.page.url.startswith(Config.CART_URL)