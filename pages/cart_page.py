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
        self.page.click(self.add_to_cart_button)
        self.page.wait_for_selector(self.view_cart_button)
        self.page.click(self.view_cart_button)

    def is_cart_page(self) -> bool:
        return self.page.url.startswith(Config.CART_URL)
