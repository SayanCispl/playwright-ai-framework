import pytest
import allure
from pages.search import SearchPage

@pytest.mark.desktop
@allure.feature("Search")
@allure.story("Search for product - Blue Top")
@allure.severity(allure.severity_level.CRITICAL)
def test_search_blue_top(page):
    search_page = SearchPage(page)

    with allure.step("Login and navigate to product search page"):
        search_page.login_and_navigate()

    with allure.step("Search for 'Blue Top'"):
        search_page.search_product("Blue Top")
        allure.attach(page.screenshot(), name="Search Results", attachment_type=allure.attachment_type.PNG)

    with allure.step("Verify at least one correct product is displayed"):
        assert search_page.is_correct_product_displayed("Blue Top")

    with allure.step("Verify all results are relevant to 'Blue Top'"):
        assert search_page.are_all_results_relevant("Blue Top")
        allure.attach("\n".join(search_page.get_all_product_names()),
                      name="All Product Names",
                      attachment_type=allure.attachment_type.TEXT)


@pytest.mark.desktop
@allure.feature("Search")
@allure.story("Search for non-existent product")
@allure.severity(allure.severity_level.MINOR)
def test_search_non_existent_product(page):
    search_page = SearchPage(page)

    with allure.step("Login and navigate to product search page"):
        search_page.login_and_navigate()

    with allure.step("Search for 'Purple Jacket' (non-existent)"):
        search_page.search_product("Purple Jacket")
        allure.attach(page.screenshot(), name="Search Results - Negative Case", attachment_type=allure.attachment_type.PNG)

    with allure.step("Verify no results are displayed"):
        assert search_page.has_no_results()
