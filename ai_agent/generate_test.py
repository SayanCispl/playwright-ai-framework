def generate_login_test():
    return '''
def test_login(page):
    page.goto("https://automationexercise.com/login")
    page.fill("#username", "test_t101@yopmail.com")
    page.fill("#password", "Test@123")
    page.click("text=Login")
    assert page.url == "https://automationexercise.com/dashboard"
'''
