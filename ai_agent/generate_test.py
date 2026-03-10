def generate_login_test():
    return '''
def test_login(page):
    page.goto("https://demo.playwright.dev/login")
    page.fill("#username", "user")
    page.fill("#password", "pass")
    page.click("text=Login")
    assert page.url == "https://demo.playwright.dev/dashboard"
'''
