import pytest
import os
import allure

def pytest_configure(config):
    """
    Register custom markers so pytest doesn't complain.
    """
    config.addinivalue_line("markers", "desktop: run test on desktop browsers")
    config.addinivalue_line("markers", "mobile: run test on mobile devices")

@pytest.fixture(scope="session", autouse=True)
def allure_environment_setup():
    """
    Write environment.properties file for Allure reports.
    Runs once per test session.
    """
    results_dir = os.getenv("ALLURE_RESULTS_DIR", "reports")
    os.makedirs(results_dir, exist_ok=True)
    env_file = os.path.join(results_dir, "environment.properties")

    with open(env_file, "w") as f:
        f.write("OS=Cross-OS (Ubuntu, Windows, macOS)\n")
        f.write("Browser=Chromium / Firefox / WebKit\n")
        f.write("Framework=pytest-playwright\n")

# Disable animations globally for all tests to improve stability and speed.
# Also block ads to prevent overlapping during click actions.
@pytest.fixture(autouse=True)
def setup_page(page):
    # Route to abort ad requests
    blocked_domains = [
        "doubleclick.net",
        "googlesyndication.com",
        "adservice.google.com",
        "googletagservices.com"
    ]
    def handle_route(route):
        if any(domain in route.request.url for domain in blocked_domains):
            route.abort()
        else:
            route.fallback()

    page.route("**/*", handle_route)

    # Disable CSS animations/transitions in CI and hide ad elements
    page.add_init_script("""
        document.addEventListener('DOMContentLoaded', () => {
            const style = document.createElement('style');
            style.innerHTML = `
                *, *::before, *::after {
                    animation-duration: 0s !important;
                    transition-duration: 0s !important;
                }
                iframe[id^="aswift"],
                iframe[name^="aswift"],
                ins.adsbygoogle,
                div[id^="google_ads"] {
                    display: none !important;
                }
            `;
            document.head.appendChild(style);
        });
    """)

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook to capture screenshots on test failure.
    Runs after each test phase (setup, call, teardown).
    """
    outcome = yield
    report = outcome.get_result()

    # Only act on actual test call failures
    if report.when == "call" and report.failed:
        page = item.funcargs.get("page", None)
        if page:
            screenshot_path = f"screenshots/{item.name}.png"
            os.makedirs("screenshots", exist_ok=True)
            page.screenshot(path=screenshot_path)
            allure.attach.file(
                screenshot_path,
                name=f"Failure Screenshot - {item.name}",
                attachment_type=allure.attachment_type.PNG
            )
