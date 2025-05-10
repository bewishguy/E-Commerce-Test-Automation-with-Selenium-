import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.helpers import wait_for_element
from utils.registration import register_user_with_address
from pages.checkout_page import CheckoutPage
from pages.products_page import ProductsPage
from pages.product_detail_page import ProductDetailPage

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    })
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def login_existing_user(driver):
    driver.get("https://automationexercise.com")
    driver.find_element(By.LINK_TEXT, "Signup / Login").click()
    driver.find_element(By.NAME, "email").send_keys("your_email@example.com")
    driver.find_element(By.NAME, "password").send_keys("your_password")
    driver.find_element(By.XPATH, "//button[text()='Login']").click()
    time.sleep(2)

    driver.find_element(By.XPATH, "//a[@href='/products']").click()
    time.sleep(2)
    driver.execute_script("window.scrollBy(0, 600);")
    wait_for_element(driver, By.XPATH, "(//a[text()='Add to cart'])[1]").click()
    time.sleep(1)
    wait_for_element(driver, By.XPATH, "//button[text()='Continue Shopping']").click()

    driver.find_element(By.XPATH, "//a[@href='/view_cart']").click()
    wait_for_element(driver, By.XPATH, "//a[text()='Proceed To Checkout']").click()
    time.sleep(2)

    return CheckoutPage(driver)


# TC02: Show the correct selected products
def test_tc02_product_summary_displayed(login_existing_user):
    checkout_page = login_existing_user
    assert checkout_page.is_product_summary_displayed(), "❌ Product summary not displayed"


# TC03 + TC04 comment&Place Order
def test_tc03_tc04_enter_comment_and_place_order(driver):
    email, password = register_user_with_address(driver)

    driver.get("https://automationexercise.com/products")
    time.sleep(2)

    # Add product to cart
    driver.execute_script("window.scrollBy(0, 600);")
    add_to_cart_btn = wait_for_element(driver, By.XPATH, "(//a[text()='Add to cart'])[1]")
    add_to_cart_btn.click()
    time.sleep(1)

    # Click View Cart
    view_cart = wait_for_element(driver, By.XPATH, "//u[text()='View Cart']")
    view_cart.click()

    # Click Proceed to Checkout
    checkout_btn = wait_for_element(driver, By.XPATH, "//a[text()='Proceed To Checkout']")
    checkout_btn.click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "cart_info")))

    with open("page_source.html", "w", encoding="utf-8") as f:
        f.write(driver.page_source)
    print("Current URL:", driver.current_url)

    checkout_page = CheckoutPage(driver)
    assert checkout_page.is_product_summary_displayed(), "❌ Product summary not visible"
    assert checkout_page.enter_comment("This is a test comment."), "❌ Failed to enter comment"
    assert checkout_page.click_place_order(), "❌ Failed to click Place Order"
    assert "payment" in driver.current_url.lower(), "❌ Did not navigate to payment page"

# def test_tc05_verify_checkout_address(driver):
#     # Register and get expected address
#     email, password, expected_address = register_user_with_address(driver)

#     # Add product to cart
#     driver.find_element(By.LINK_TEXT, "Products").click()
#     driver.execute_script("window.scrollBy(0, 600);")
#     driver.find_element(By.XPATH, "(//a[text()='Add to cart'])[1]").click()
#     WebDriverWait(driver, 5).until(
#         EC.element_to_be_clickable((By.XPATH, "//button[text()='Continue Shopping']"))
#     ).click()

#     # View cart
#     driver.find_element(By.XPATH, "//a[@href='/view_cart']").click()
#     driver.find_element(By.XPATH, "//a[text()='Proceed To Checkout']").click()

#     # รอให้หน้า Checkout โหลดครบก่อนดึง address
#     WebDriverWait(driver, 10).until(
#         EC.visibility_of_element_located((By.XPATH, "//h2[text()='Review Your Order']"))
#     )
#     WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.XPATH, "//ul[@id='address_delivery']"))
#     )
#     WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.XPATH, "//ul[@id='address_invoice']"))
#     )

#     checkout_page = CheckoutPage(driver)

#     billing_address = checkout_page.get_billing_address_text()
#     delivery_address = checkout_page.get_delivery_address_text()

#     print("\nEXPECTED:\n", expected_address)
#     print("\nACTUAL (Billing):\n", billing_address)
#     print("\nACTUAL (Delivery):\n", delivery_address)

#     assert expected_address in billing_address, "❌ Billing address does not match!"
#     assert expected_address in delivery_address, "❌ Delivery address does not match!"