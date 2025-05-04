import pytest
from selenium import webdriver
from pages.products_page import ProductsPage
from test_data.testdata_products import expected_min_products
from pages.product_detail_page import ProductDetailPage

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