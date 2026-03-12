import pytest
import allure
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from logs.test_run import log_test_start, log_test_success, log_test_failure


@pytest.mark.desktop
@allure.feature("Cart")
@allure.story("Add product to cart")
@allure.severity(allure.severity_level.CRITICAL)
def test_add_to_cart(page):
    test_name = "Add to Cart Test"
    log_test_start(test_name)

    try:
        with allure.step("Login to application"):
            login_page = LoginPage(page)
            login_page.navigate()
            login_page.login()
            allure.attach(page.screenshot(), name="After Login", attachment_type=allure.attachment_type.PNG)
            assert login_page.is_logged_in()

        with allure.step("Add product and navigate to cart"):
            cart_page = CartPage(page)
            cart_page.navigate()
            cart_page.add_item_to_cart()
            allure.attach(page.screenshot(), name="Cart Screenshot", attachment_type=allure.attachment_type.PNG)

        with allure.step("Verify cart page loaded"):
            assert page.url.endswith("/view_cart")
            allure.attach(page.url, name="Cart URL", attachment_type=allure.attachment_type.TEXT)

        log_test_success(test_name)
    except Exception as e:
        page.screenshot(path="screenshots/cart_failure.png")
        allure.attach.file("screenshots/cart_failure.png", name="Failure Screenshot", attachment_type=allure.attachment_type.PNG)
        log_test_failure(test_name, str(e))
        raise


@pytest.mark.desktop
@allure.feature("Cart")
@allure.story("Add product to cart - Desktop")
@allure.severity(allure.severity_level.NORMAL)
def test_add_to_cart_desktop(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login()
    cart_page = CartPage(page)
    cart_page.navigate()
    cart_page.add_item_to_cart()
    allure.attach(page.screenshot(), name="Desktop Cart Screenshot", attachment_type=allure.attachment_type.PNG)
    assert page.url.endswith("/view_cart")


#@pytest.mark.mobile
#@allure.feature("Cart")
#@allure.story("Add product to cart - Mobile")
#@allure.severity(allure.severity_level.NORMAL)
#def test_add_to_cart_mobile(page):
#    login_page = LoginPage(page)
#    login_page.navigate()
#    login_page.login()
#    cart_page = CartPage(page)
#    cart_page.navigate()
#    cart_page.add_item_to_cart()
#    allure.attach(page.screenshot(), name="Mobile Cart Screenshot", attachment_type=allure.attachment_type.PNG)
#    assert page.url.endswith("/view_cart")