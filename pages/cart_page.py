from playwright.sync_api import Page
from config.config import Config

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        # Example selectors (adjust if needed after inspecting site)
        self.add_to_cart_button = "(//a[contains(text(),'Add to cart')])[1]"  # first product
        self.cart_link = "a[href='/view_cart']"
        self.cart_count = "span#cart_items"  # adjust if site uses different element

    def navigate(self):
        self.page.goto(Config.SHOP_URL)

    def add_item_to_cart(self):
        self.page.click(self.add_to_cart_button)

    def go_to_cart(self):
        self.page.click(self.cart_link)

    def get_cart_count(self) -> str:
        return self.page.inner_text(self.cart_count)
