from config.config import Config
from pages.login_page import LoginPage

class SearchPage:
    def __init__(self, page):
        self.page = page
        self.search_input = "input#search_product"
        self.search_button = "button#submit_search"
        self.product_name_locator = "div.productinfo.text-center p"

    def login_and_navigate(self):
        """Login first, then navigate to the products page."""
        login_page = LoginPage(self.page)
        login_page.navigate()
        login_page.login()
        assert login_page.is_logged_in(), "Login failed"
        self.page.goto(Config.SHOP_URL)

    def search_product(self, product_name: str):
        self.page.fill(self.search_input, product_name)
        self.page.click(self.search_button)

    def get_all_product_names(self):
        return self.page.locator(self.product_name_locator).all_inner_texts()

    def is_correct_product_displayed(self, expected_name: str) -> bool:
        product_names = self.get_all_product_names()
        return any(expected_name.lower() in name.lower() for name in product_names)

    def are_all_results_relevant(self, keyword: str) -> bool:
        product_names = self.get_all_product_names()
        return all(keyword.lower() in name.lower() for name in product_names)

    def has_no_results(self) -> bool:
        return self.page.locator(self.product_name_locator).count() == 0
