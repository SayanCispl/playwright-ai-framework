from pages.cart_page import CartPage
from pages.login_page import LoginPage
from logs.test_run import log_test_start, log_test_success, log_test_failure

def test_add_to_cart(page):
    test_name = "Add to Cart Test"
    log_test_start(test_name)

    try:
        # Login first
        login_page = LoginPage(page)
        login_page.navigate()
        login_page.login()
        assert login_page.is_logged_in()

        # Navigate to cart/shop
        cart_page = CartPage(page)
        cart_page.navigate()
        cart_page.add_item_to_cart()
        assert cart_page.get_cart_count() == "1"

        log_test_success(test_name)
    except Exception as e:
        page.screenshot(path="screenshots/cart_failure.png")
        log_test_failure(test_name, str(e))
        raise
