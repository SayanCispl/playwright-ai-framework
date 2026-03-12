import allure
import pytest
from pages.login_page import LoginPage

@pytest.mark.desktop
@allure.feature("Authentication")
@allure.story("Valid login")
@allure.severity(allure.severity_level.BLOCKER)
def test_login(page):
    login = LoginPage(page)

    with allure.step("Navigate to login page"):
        login.navigate()

    with allure.step("Enter credentials and submit"):
        login.login()
        allure.attach(page.screenshot(), name="Login Attempt", attachment_type=allure.attachment_type.PNG)

    with allure.step("Verify login success"):
        assert login.is_logged_in()
        allure.attach(page.url, name="Final URL", attachment_type=allure.attachment_type.TEXT)

@pytest.mark.desktop
@allure.feature("Authentication")
@allure.story("Login on desktop")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.desktop
def test_login_desktop(page):
        login_page = LoginPage(page)
        login_page.navigate()
        login_page.login()
        assert login_page.is_logged_in()

#@pytest.mark.mobile
#@allure.feature("Authentication")
#@allure.story("Login on mobile")
#@allure.severity(allure.severity_level.NORMAL)
#@pytest.mark.mobile
#def test_login_mobile(page):
#        login_page = LoginPage(page)
#        login_page.navigate()
#        login_page.login()
#        assert login_page.is_logged_in()
