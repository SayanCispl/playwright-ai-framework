import pytest
import allure
from api.api_client import ApiClient
from config.config import Config

@allure.feature("API")
@allure.story("Get All Products")
@allure.severity(allure.severity_level.CRITICAL)
def test_get_products_list():
    """
    Test Case: Verify that the products list API returns status 200
    and contains a 'products' key in the JSON response.
    """
    response = ApiClient.get_products_list()
    assert response.status_code == 200
    data = response.json()
    allure.attach(str(data), name="Products List", attachment_type=allure.attachment_type.JSON)
    assert "products" in data


@allure.feature("API")
@allure.story("Register User")
@allure.severity(allure.severity_level.NORMAL)
def test_register_user():
    """
    Test Case: Register a new user via API.
    Expected: Response code 200/201 and message 'User created!' or 'already exists'.
    """
    payload = {
        "name": "Test User",
        "email": "test_user_api@yopmail.com",
        "password": "Test@123",
        "title": "Mr",
        "birth_date": "1",
        "birth_month": "1",
        "birth_year": "1990",
        "firstname": "Test",
        "lastname": "User",
        "company": "QA Inc",
        "address1": "123 Test Street",
        "address2": "Suite 1",
        "country": "India",
        "zipcode": "700001",
        "state": "WB",
        "city": "Kolkata",
        "mobile_number": "9999999999"
    }
    response = ApiClient.register_user(payload)
    assert response.status_code in [200, 201]
    allure.attach(response.text, name="Register Response", attachment_type=allure.attachment_type.TEXT)
    assert "User created" in response.text or "already exists" in response.text


@allure.feature("API")
@allure.story("Verify Login")
@allure.severity(allure.severity_level.CRITICAL)
def test_verify_login():
    """
    Test Case: Verify login API with valid credentials.
    Expected: Response code 200 and message 'User exists!'.
    """
    response = ApiClient.verify_login(Config.USERNAME, Config.PASSWORD)
    assert response.status_code == 200
    allure.attach(response.text, name="Login Verify Response", attachment_type=allure.attachment_type.TEXT)
    assert "User exists" in response.text


@allure.feature("API")
@allure.story("Search Product API")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("keyword", ["top", "tshirt", "jean"])
def test_search_product(keyword):
    """
    Test Case: Search for products via API using keywords.
    Expected: Response code 200 and products list containing the keyword.
    """
    response = ApiClient.search_product(keyword)
    assert response.status_code == 200
    data = response.json()
    allure.attach(str(data), name=f"Search Results for {keyword}", attachment_type=allure.attachment_type.JSON)
    assert "products" in data
    assert any(keyword.lower() in p["name"].lower() for p in data["products"])
