from pages.login_page import LoginPage
from logs.test_run import log_test_start, log_test_success, log_test_failure

def test_login(page):
    test_name = "Login Test"
    log_test_start(test_name)

    try:
        login_page = LoginPage(page)
        login_page.navigate()
        login_page.login()
        assert login_page.is_logged_in()
        log_test_success(test_name)
    except Exception as e:
        page.screenshot(path="screenshots/login_failure.png")
        log_test_failure(test_name, str(e))
        raise
