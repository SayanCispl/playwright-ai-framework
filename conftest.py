import pytest
import allure

def pytest_configure(config):
    """
    Register custom markers so pytest doesn't complain.
    """
    config.addinivalue_line("markers", "desktop: run test on desktop browsers")
    config.addinivalue_line("markers", "mobile: run test on mobile devices")

@pytest.fixture(autouse=True)
def allure_environment():
    """
    Attach environment info to Allure reports.
    This runs automatically for every test.
    """
    allure.environment(
        OS="Cross-OS (Ubuntu, Windows, macOS)",
        Browser="Chromium / Firefox / WebKit",
        Framework="pytest-playwright",
    )
