import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.helpers import wait_for_element
from utils.registration import register_user_with_full_address
from pages.checkout_page import CheckoutPage

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options)
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

def test_tc21_product_summary_displayed(login_existing_user):
    checkout_page = login_existing_user
    assert checkout_page.is_product_summary_displayed(), "Product summary not displayed"

def test_tc22_to_tc25_register_checkout_payment(driver):
    email, password, expected_address = register_user_with_full_address(driver)

    WebDriverWait(driver, 20).until(
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

    # TC22
    checkout_page = CheckoutPage(driver)
    billing_address = checkout_page.get_billing_address_text()
    delivery_address = checkout_page.get_delivery_address_text()
    assert expected_address in billing_address, "Billing address mismatch!"
    assert expected_address in delivery_address, "Delivery address mismatch!"

    # TC23-TC24
    comment_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "message"))
    )
    comment_box.send_keys("Automated comment for test")
    place_order_btn = driver.find_element(By.XPATH, "//a[text()='Place Order']")
    driver.execute_script("arguments[0].click();", place_order_btn)

    # TC25
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h2[text()='Payment']"))
    )
    driver.find_element(By.NAME, "name_on_card").send_keys("Test User")
    driver.find_element(By.NAME, "card_number").send_keys("4111111111111111")
    driver.find_element(By.NAME, "cvc").send_keys("123")
    driver.find_element(By.NAME, "expiry_month").send_keys("12")
    driver.find_element(By.NAME, "expiry_year").send_keys("2030")
    driver.find_element(By.ID, "submit").click()

    confirm_text = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//p[contains(text(),'Congratulations! Your order has been confirmed!')]"))
    )
    assert "order has been confirmed" in confirm_text.text.lower(), "Confirmation not found"
