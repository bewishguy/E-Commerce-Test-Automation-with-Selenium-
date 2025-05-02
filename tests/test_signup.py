import time
import pytest
from selenium.webdriver.common.by import By
from test_data.testdata_signup import generate_signup_data
from pages.signup_page import SignupPage

@pytest.mark.signup
def test_signup(driver):
    # Load test data
    data = generate_signup_data()
    name = data["name"]
    email = data["email"]
    password = data["password"]

    # ----------- Case 1: Successful Signup -----------
    driver.get("https://automationexercise.com/signup")

    page = SignupPage(driver)
    page.enter_name(name)
    page.enter_email(email)
    page.click_signup()

    time.sleep(2)
    assert "Enter Account Information" in driver.page_source

    # Fill account information
    driver.find_element(By.ID, "id_gender1").click()
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.NAME, "days").send_keys("1")
    driver.find_element(By.NAME, "months").send_keys("January")
    driver.find_element(By.NAME, "years").send_keys("2000")
    driver.find_element(By.ID, "newsletter").click()
    driver.find_element(By.ID, "first_name").send_keys("TestFirst")
    driver.find_element(By.ID, "last_name").send_keys("TestLast")
    driver.find_element(By.ID, "address1").send_keys("123 Test Street")
    driver.find_element(By.ID, "country").send_keys("United States")
    driver.find_element(By.ID, "state").send_keys("California")
    driver.find_element(By.ID, "city").send_keys("Los Angeles")
    driver.find_element(By.ID, "zipcode").send_keys("90001")
    driver.find_element(By.ID, "mobile_number").send_keys("1234567890")
    driver.find_element(By.XPATH, "//button[@data-qa='create-account']").click()

    assert "Account Created!" in driver.page_source

    # ----------- Case 2: Re-register with existing email -----------
    driver.get("https://automationexercise.com/signup")
    page.enter_name(name)
    page.enter_email(email)  # Use same email again
    page.click_signup()

    time.sleep(2)
    assert "Email Address already exist!" in driver.page_source