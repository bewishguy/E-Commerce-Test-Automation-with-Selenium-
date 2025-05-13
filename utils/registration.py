# import time
from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

fake = Faker()

def register_user_with_address(driver):
    email = fake.email()
    password = "Test1234"

    driver.get("https://automationexercise.com")
    driver.find_element(By.LINK_TEXT, "Signup / Login").click()

    driver.find_element(By.CSS_SELECTOR, "input[data-qa='signup-name']").send_keys(fake.first_name())
    driver.find_element(By.CSS_SELECTOR, "input[data-qa='signup-email']").send_keys(email)
    driver.find_element(By.XPATH, "//button[text()='Signup']").click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "id_gender1"))).click()
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "days").send_keys("10")
    driver.find_element(By.ID, "months").send_keys("May")
    driver.find_element(By.ID, "years").send_keys("1990")

    driver.find_element(By.ID, "first_name").send_keys(fake.first_name())
    driver.find_element(By.ID, "last_name").send_keys(fake.last_name())
    driver.find_element(By.ID, "company").send_keys(fake.company())
    driver.find_element(By.ID, "address1").send_keys(fake.street_address())
    driver.find_element(By.ID, "address2").send_keys("Suite 123")
    driver.find_element(By.ID, "state").send_keys("California")
    driver.find_element(By.ID, "city").send_keys("Los Angeles")
    driver.find_element(By.ID, "zipcode").send_keys("90001")
    driver.find_element(By.ID, "mobile_number").send_keys(fake.phone_number())

    driver.find_element(By.XPATH, "//button[text()='Create Account']").click()

    # Continue
    continue_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[text()='Continue']"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", continue_btn)
    driver.execute_script("arguments[0].click();", continue_btn)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Logout"))
    )

    return email, password

def register_user_with_full_address(driver):
    email = fake.email()
    password = "Test1234"

    driver.get("https://automationexercise.com")

    driver.find_element(By.LINK_TEXT, "Signup / Login").click()

    driver.find_element(By.CSS_SELECTOR, "input[data-qa='signup-name']").send_keys(fake.first_name())
    driver.find_element(By.CSS_SELECTOR, "input[data-qa='signup-email']").send_keys(email)
    driver.find_element(By.XPATH, "//button[text()='Signup']").click()

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "id_gender1"))).click()
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "days").send_keys("10")
    driver.find_element(By.ID, "months").send_keys("May")
    driver.find_element(By.ID, "years").send_keys("1990")

    first_name = fake.first_name()
    last_name = fake.last_name()
    company = fake.company()
    address1 = fake.street_address()
    address2 = "Suite 123"
    state = "California"
    city = "Los Angeles"
    zipcode = "90001"
    mobile = fake.phone_number()
    country = "United States"

    driver.find_element(By.ID, "first_name").send_keys(first_name)
    driver.find_element(By.ID, "last_name").send_keys(last_name)
    driver.find_element(By.ID, "company").send_keys(company)
    driver.find_element(By.ID, "address1").send_keys(address1)
    driver.find_element(By.ID, "address2").send_keys(address2)
    driver.find_element(By.ID, "state").send_keys(state)
    driver.find_element(By.ID, "city").send_keys(city)
    driver.find_element(By.ID, "zipcode").send_keys(zipcode)
    driver.find_element(By.ID, "mobile_number").send_keys(mobile)

    Select(driver.find_element(By.ID, "country")).select_by_visible_text(country)
    driver.find_element(By.XPATH, "//button[text()='Create Account']").click()

    continue_btn = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//a[text()='Continue']"))
    )
    driver.execute_script("arguments[0].click();", continue_btn)

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.LINK_TEXT, "Logout")))

    full_address = f"{first_name} {last_name}\n{company}\n{address1}\n{address2}\n{city} {state} {zipcode}\nUnited States\n{mobile}"
    return email, password, full_address.strip()