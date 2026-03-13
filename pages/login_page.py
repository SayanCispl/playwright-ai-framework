from playwright.sync_api import Page
from config.config import Config


class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self) -> None:
        """
        Navigate to the login page.
        """
        self.page.goto(Config.LOGIN_URL)
        self.page.wait_for_load_state("networkidle")

    def login(self, username: str = Config.USERNAME, password: str = Config.PASSWORD) -> None:
        """
        Perform login with the given credentials.

        Args:
            username (str): The username to log in with.
            password (str): The password to log in with.
        """
        # Wait for login form to be ready
        self.page.wait_for_selector("[data-qa='login-email']", state="visible")

        self.page.fill("[data-qa='login-email']", username)
        self.page.fill("[data-qa='login-password']", password)
        self.page.click("[data-qa='login-button']")

        # Wait for navigation to dashboard
        self.page.wait_for_url(f"**{Config.DASHBOARD_URL}**")
        self.page.wait_for_load_state("networkidle")

    def is_logged_in(self) -> bool:
        """
        Check if the user is logged in by verifying the current URL.

        Returns:
            bool: True if logged in, False otherwise.
        """
        return self.page.url.startswith(Config.DASHBOARD_URL)