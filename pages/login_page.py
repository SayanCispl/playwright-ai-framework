from playwright.sync_api import Page
from config.config import Config

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        # Using provided XPaths
        self.email_input = "//input[@data-qa='login-email']"
        self.password_input = "//input[@data-qa='login-password']"
        self.login_button = "//button[@data-qa='login-button']"

    def navigate(self):
        self.page.goto(Config.LOGIN_URL)

    def login(self, username: str = Config.USERNAME, password: str = Config.PASSWORD):
        self.page.fill(self.email_input, username)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)

    def is_logged_in(self) -> bool:
        # After login, check if redirected to home/dashboard
        return self.page.url.startswith(Config.DASHBOARD_URL)
