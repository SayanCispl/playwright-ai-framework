class Config:
    BASE_URL = "https://automationexercise.com"
    LOGIN_URL = f"{BASE_URL}/login"
    SHOP_URL = f"{BASE_URL}/products"
    CART_URL = f"{BASE_URL}/view_cart"
    DASHBOARD_URL = f"{BASE_URL}/"
    CONFIRMATION_URL = f"{BASE_URL}/payment_done"

    # Login credentials
    USERNAME = "test_t101@yopmail.com"
    PASSWORD = "Test@123"

    # Paths
    LOG_PATH = "logs/"
    REPORT_PATH = "reports/"
    SCREENSHOT_PATH = "screenshots/"
