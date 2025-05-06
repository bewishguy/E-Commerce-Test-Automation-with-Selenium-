import time
import pytest
from selenium import webdriver
from checkout_page import CheckoutPage
from testdata_checkout import checkout_comment_text

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://automationexercise.com")
    yield driver
    driver.quit()

@pytest.fixture
def login_and_go_to_checkout(driver):
    # Login
    driver.find_element("link text", "Signup / Login").click()
    driver.find_element("name", "email").send_keys("your_email@example.com")
    driver.find_element("name", "password").send_keys("your_password")
    driver.find_element("xpath", "//button[text()='Login']").click()
    time.sleep(2)

    # Add Product to Cart
    driver.find_element("xpath", "//a[@href='/products']").click()
    time.sleep(2)
    driver.execute_script("window.scrollBy(0, 600);")
    driver.find_element("xpath", "(//a[text()='Add to cart'])[1]").click()
    time.sleep(1)
    driver.find_element("xpath", "//button[text()='Continue Shopping']").click()

    # Go to Cart & Checkout
    driver.find_element("xpath", "//a[@href='/view_cart']").click()
    driver.find_element("xpath", "//a[text()='Proceed To Checkout']").click()
    time.sleep(2)

    return CheckoutPage(driver)

# TC02: แสดงสินค้าที่เลือกถูกต้อง
def test_tc02_product_summary_displayed(login_and_go_to_checkout):
    checkout_page = login_and_go_to_checkout
    assert checkout_page.is_product_summary_displayed(), "❌ Product summary not displayed"

# TC03: กรอกข้อความในช่อง Comment
def test_tc03_enter_comment(login_and_go_to_checkout):
    checkout_page = login_and_go_to_checkout
    checkout_page.enter_comment(checkout_comment_text)
    time.sleep(1)

# TC04: กดปุ่ม Place Order แล้วไปหน้าชำระเงิน
def test_tc04_place_order_navigates_to_payment(login_and_go_to_checkout, driver):
    checkout_page = login_and_go_to_checkout
    checkout_page.click_place_order()
    time.sleep(2)
    assert "payment" in driver.current_url.lower(), "❌ Did not navigate to payment page"
