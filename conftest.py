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
