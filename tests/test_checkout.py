def test_checkout(page):
    page.goto("https://demo.playwright.dev/cart")
    page.click("text=Checkout")
    assert page.url == "https://demo.playwright.dev/confirmation"
