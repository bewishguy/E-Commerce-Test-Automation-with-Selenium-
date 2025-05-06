import pytest
from selenium import webdriver
from pages.products_page import ProductsPage
from selenium.webdriver.common.by import By
from test_data.testdata_products import expected_min_products
from pages.product_detail_page import ProductDetailPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    # Setup
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    driver.get("https://automationexercise.com/")
    yield driver
    # Teardown
    driver.quit()

def test_TC08_verify_all_products_displayed(driver):
    products_page = ProductsPage(driver)
    products_page.go_to_products_page()
    products = products_page.get_all_products()

    print(f"Found {len(products)} products on the page.")
    assert len(products) >= expected_min_products, "Not all products are displayed"

def test_TC09_verify_each_product_has_name_price_and_add_to_cart(driver):
    products_page = ProductsPage(driver)
    products_page.go_to_products_page()

    names = products_page.get_product_names()
    prices = products_page.get_product_prices()
    product_count = len(names)

    assert product_count > 0, "No products found"
    assert len(prices) == product_count, "Mismatch in product price count"

    for i in range(product_count):
        assert names[i].is_displayed(), f"Product name at index {i} not visible"
        assert prices[i].is_displayed(), f"Product price at index {i} not visible"

        # Hover
        products_page.hover_over_product(i)
        add_to_cart_buttons = products_page.get_add_to_cart_overlay_buttons()
        assert len(add_to_cart_buttons) > i, f"Missing Add to Cart button at index {i}"
        assert add_to_cart_buttons[i].is_displayed(), f"Add to Cart button at index {i} not visible"
        
def test_TC10_click_view_product_goes_to_detail_page(driver):
    products_page = ProductsPage(driver)
    products_page.go_to_products_page()

    products_page.click_view_product_by_index(0)

    product_detail_page = ProductDetailPage(driver)
    product_name = product_detail_page.get_product_name()

    assert product_name is not None and product_name.strip() != "", "Product name not found on detail page"
    print(f"Product detail page loaded with name: {product_name}")

def test_TC11_search_existing_product(driver):
    products_page = ProductsPage(driver)
    products_page.go_to_products_page()

    search_keyword = "top"
    products_page.search_product(search_keyword)

    result_names = products_page.get_search_results_names()
    assert len(result_names) > 0, f"No results found for keyword '{search_keyword}'"

    for i, name_element in enumerate(result_names):
        print(f"[{i}] {name_element.text}")
    match_count = 0
    for name_element in result_names:
        if search_keyword.lower() in name_element.text.lower():
            match_count += 1

    assert match_count > 0, f"No matching items found that include the keyword '{search_keyword}'"

def test_TC12_search_non_existing_product(driver):
    products_page = ProductsPage(driver)
    products_page.go_to_products_page()

    search_keyword = "invalidproduct"
    products_page.search_product(search_keyword)

    result_names = products_page.get_search_results_names()
    assert len(result_names) == 0, f"Expected no results, but found {len(result_names)} products"

def test_TC13_filter_by_category_women_tops(driver):
    products_page = ProductsPage(driver)
    products_page.go_to_products_page()

    products_page.click_category_women_tops()
    result_names = products_page.get_category_products_names()

    assert len(result_names) > 0, "No products found under Women > Tops category"

    for i, name_element in enumerate(result_names):
        print(f"[{i}] {name_element.text}")

def test_TC14_add_to_cart_shows_popup(driver):
    products_page = ProductsPage(driver)
    products_page.go_to_products_page()

    products_page.hover_and_add_first_product_to_cart()

    assert products_page.is_add_to_cart_modal_visible(), "Add to cart modal did not appear"

    products_page.close_cart_modal()
