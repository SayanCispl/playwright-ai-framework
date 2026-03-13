import requests
from config.config import Config

class ApiClient:
    """
    API Client layer for AutomationExercise endpoints.
    Provides reusable static methods for GET/POST requests.
    """

    BASE_URL = Config.BASE_URL

    @staticmethod
    def get_products_list():
        """
        GET /api/productsList
        Returns all products available in the system.
        """
        url = f"{ApiClient.BASE_URL}/api/productsList"
        response = requests.get(url)
        return response

    @staticmethod
    def register_user(payload: dict):
        """
        POST /api/createAccount
        Registers a new user with the given payload.
        Payload must include name, email, password, and other required fields.
        """
        url = f"{ApiClient.BASE_URL}/api/createAccount"
        response = requests.post(url, data=payload)
        return response

    @staticmethod
    def verify_login(email: str, password: str):
        """
        POST /api/verifyLogin
        Verifies login credentials for an existing user.
        """
        url = f"{ApiClient.BASE_URL}/api/verifyLogin"
        response = requests.post(url, data={"email": email, "password": password})
        return response

    @staticmethod
    def search_product(keyword: str):
        """
        POST /api/searchProduct
        Searches for products by keyword (e.g., 'top', 'tshirt', 'jean').
        """
        url = f"{ApiClient.BASE_URL}/api/searchProduct"
        response = requests.post(url, data={"search_product": keyword})
        return response
