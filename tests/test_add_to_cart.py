def test_add_to_cart(page):
    page.goto("https://demo.playwright.dev/shop")
    page.click("text=Add to Cart")
    assert page.inner_text("#cart-count") == "1"
