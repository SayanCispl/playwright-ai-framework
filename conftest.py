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
