import pytest
import allure
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.mark.desktop
@allure.feature("Checkout Flow")
@allure.story("Valid checkout after login")
@allure.severity(allure.severity_level.CRITICAL)
def test_full_checkout_flow(page):
    with allure.step("Navigate to login page and login"):
        login = LoginPage(page)
        login.navigate()
        login.login()
        allure.attach(page.screenshot(), name="After Login", attachment_type=allure.attachment_type.PNG)
        assert login.is_logged_in()

    with allure.step("Add item to cart"):
        cart = CartPage(page)
        cart.navigate()
        cart.add_item_to_cart()
        allure.attach(page.screenshot(), name="Cart Screenshot", attachment_type=allure.attachment_type.PNG)
        assert cart.is_cart_page()

    with allure.step("Proceed to checkout"):
        checkout = CheckoutPage(page)
        checkout.navigate()
        checkout.checkout()
        allure.attach(page.screenshot(), name="Checkout Screenshot", attachment_type=allure.attachment_type.PNG)
        assert checkout.is_checkout_page()

@pytest.mark.desktop
@allure.feature("Checkout Flow")
@allure.story("Checkout on desktop")
@allure.severity(allure.severity_level.NORMAL)
def test_checkout_desktop(page):
        login_page = LoginPage(page)
        login_page.navigate()
        login_page.login()
        cart_page = CartPage(page)
        cart_page.navigate()
        cart_page.add_item_to_cart()
        checkout_page = CheckoutPage(page)
        checkout_page.navigate()
        checkout_page.checkout()
        assert checkout_page.is_checkout_page()


#@pytest.mark.mobile
#@allure.feature("Checkout Flow")
#@allure.story("Checkout on mobile")
#@allure.severity(allure.severity_level.NORMAL)
#@pytest.mark.mobile
#def test_checkout_mobile(page):
#        login_page = LoginPage(page)
#        login_page.navigate()
#        login_page.login()
#        cart_page = CartPage(page)
#        cart_page.navigate()
#        cart_page.add_item_to_cart()
#        checkout_page = CheckoutPage(page)
#        checkout_page.navigate()
#        checkout_page.checkout()
#        assert checkout_page.is_checkout_page()