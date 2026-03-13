import platform
import allure
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture
def page(request):
    with sync_playwright() as p:
        # Desktop flow
        if request.node.get_closest_marker("desktop"):
            browser_name = request.config.getoption("--browser") or "chromium"
            browser = getattr(p, browser_name).launch(headless=True)
            context = browser.new_context()
            page = context.new_page()
            yield page
            browser.close()

        # Mobile flow
        elif request.node.get_closest_marker("mobile"):
            device_name = request.config.getoption("--device") or "iPhone 12"
            try:
                device = p.devices[device_name]
            except KeyError:
                raise ValueError(f"Device '{device_name}' not found in Playwright presets.")
            browser = p.chromium.launch(headless=True)
            context = browser.new_context(**device)
            page = context.new_page()
            yield page
            browser.close()

        else:
            raise ValueError("Test must be marked with either @pytest.mark.desktop or @pytest.mark.mobile")

@pytest.fixture(autouse=True)
def add_suite_hierarchy(request):
    # OS detection
    os_name = platform.system()
    if os_name == "Darwin":
        os_name = "macOS"

    # Browser detection
    browser_name = request.config.getoption("--browser", default="chromium")
    if browser_name == "chromium":
        browser_label = "Chrome"
    elif browser_name == "firefox":
        browser_label = "Firefox"
    elif browser_name == "webkit":
        browser_label = "WebKit"
    else:
        browser_label = browser_name

    # Labels for filtering
    allure.dynamic.label("os", os_name)
    allure.dynamic.label("browser", browser_label)

    # Suite hierarchy: OS-Browser
    suite_name = f"{os_name}-{browser_label}"
    allure.dynamic.parent_suite(suite_name)
