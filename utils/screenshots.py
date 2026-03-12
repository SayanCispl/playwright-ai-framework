import allure
from datetime import datetime
from pathlib import Path
from playwright.sync_api import Page


def take_screenshot(page: Page, name: str) -> None:
    """
    Take a screenshot of the current page and save it with a timestamp.
    Also attaches the screenshot to the Allure report.

    Args:
        page (Page): The Playwright page object.
        name (str): Base name for the screenshot file.
    """
    timestamp = datetime.now().isoformat().replace(":", "-").replace(".", "-")
    filename = f"{name}_{timestamp}.png"
    path = Path("screenshots") / filename
    path.parent.mkdir(parents=True, exist_ok=True)  # Ensure directory exists
    page.screenshot(path=str(path))
    allure.attach.file(str(path), name=name, attachment_type=allure.attachment_type.PNG)
