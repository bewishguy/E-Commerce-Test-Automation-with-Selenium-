import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.helpers import wait_for_element
from utils.registration import register_user_with_address
from utils.registration import register_user_with_full_address
from pages.checkout_page import CheckoutPage
# from pages.payment_page import PaymentPage
# from test_data.testdata_payment import payment_data

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    options.add_experimental_option("prefs", {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False
    })
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

def test_tc02_product_summary_displayed(login_existing_user):
    checkout_page = login_existing_user
    assert checkout_page.is_product_summary_displayed(), "❌ Product summary not displayed"

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

def test_tc05_verify_checkout_address(driver):
    email, password, expected_address = register_user_with_full_address(driver)

    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//ul[@class='nav navbar-nav']"))
    )

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "features_items"))
    )

    driver.execute_script("window.scrollBy(0, 600);")

    add_btn = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "(//a[text()='Add to cart'])[1]"))
    )
    add_btn.click()

    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "modal-content"))
    )

    view_cart = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//u[text()='View Cart']"))
    )
    view_cart.click()

    checkout_btn = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//a[text()='Proceed To Checkout']"))
    )
    checkout_btn.click()

    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//h2[text()='Review Your Order']"))
    )

    checkout_page = CheckoutPage(driver)
    billing_address = checkout_page.get_billing_address_text()
    delivery_address = checkout_page.get_delivery_address_text()

    print("\nEXPECTED:\n", expected_address)
    print("\nACTUAL (Billing):\n", billing_address)
    print("\nACTUAL (Delivery):\n", delivery_address)

    assert expected_address in billing_address, "❌ Billing address does not match!"
    assert expected_address in delivery_address, "❌ Delivery address does not match!"

def test_TC08_fill_payment_information_and_confirm_order(driver):
    wait = WebDriverWait(driver, 10)

    # ✅ Step 1: เรียกใช้ register จากโค้ดเดิม
    register_user_with_full_address(driver, wait)

    # ✅ Step 2: Add to cart → Checkout → Place Order
    wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Products"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[contains(text(),'Add to cart')])[1]"))).click()
    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "View Cart"))).click()

    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Proceed To Checkout']"))).click()
    wait.until(EC.visibility_of_element_located((By.NAME, "message"))).send_keys("Please deliver ASAP.")
    driver.find_element(By.XPATH, "//a[text()='Place Order']").click()

    # ✅ Step 3: Payment
    wait.until(EC.visibility_of_element_located((By.NAME, "name_on_card"))).send_keys("Test User")
    driver.find_element(By.NAME, "card_number").send_keys("4111111111111111")
    driver.find_element(By.NAME, "cvc").send_keys("123")
    driver.find_element(By.NAME, "expiry_month").send_keys("12")
    driver.find_element(By.NAME, "expiry_year").send_keys("2027")
    driver.find_element(By.ID, "submit").click()

    # ✅ Step 4: Verify order success
    confirmation_text = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).text
    assert "Your order has been placed successfully!" in confirmation_text
    # payment_page = PaymentPage(driver)
    # driver.get("https://automationexercise.com/products")

    # # assert "payment" in driver.current_url or "payment" in driver.page_source

    # payment_page.enter_name_on_card(payment_data["name_on_card"])
    # payment_page.enter_card_number(payment_data["card_number"])
    # payment_page.enter_cvc(payment_data["cvc"])
    # payment_page.enter_expiry_month(payment_data["expiry_month"])
    # payment_page.enter_expiry_year(payment_data["expiry_year"])

    # payment_page.click_pay_button()

    # assert "Your order has been placed successfully!" in driver.page_source