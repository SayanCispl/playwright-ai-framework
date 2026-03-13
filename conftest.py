import pytest
import os

def pytest_configure(config):
    """
    Register custom markers so pytest doesn't complain.
    """
    config.addinivalue_line("markers", "desktop: run test on desktop browsers")
    config.addinivalue_line("markers", "mobile: run test on mobile devices")

@pytest.fixture(autouse=True)
def allure_environment_setup():
    """
    Write environment.properties file for Allure reports.
    This runs automatically for every test session.
    """
    results_dir = os.getenv("ALLURE_RESULTS_DIR", "reports")
    os.makedirs(results_dir, exist_ok=True)
    env_file = os.path.join(results_dir, "environment.properties")

    with open(env_file, "w") as f:
        f.write("OS=Cross-OS (Ubuntu, Windows, macOS)\n")
        f.write("Browser=Chromium / Firefox / WebKit\n")
        f.write("Framework=pytest-playwright\n")
