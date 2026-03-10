import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # set headless=True for CI
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()
