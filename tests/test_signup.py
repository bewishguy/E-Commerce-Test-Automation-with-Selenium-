from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Import ข้อมูลจากไฟล์ testdata_signup.py
from test_data.testdata_generator import generate_signup_data

def test_signup_success():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    driver.get("https://automationexercise.com/")
    driver.maximize_window()

    # Click 'Signup / Login' button
    driver.find_element(By.XPATH, "//a[contains(text(),'Signup / Login')]").click()

    # Fill in name and email for signup (ใช้ data จากไฟล์)
    driver.find_element(By.NAME, "name").send_keys(signup_data["name"])
    driver.find_element(By.XPATH, "//input[@data-qa='signup-email']").send_keys(signup_data["email"])

    # Click 'Signup' button
    driver.find_element(By.XPATH, "//button[@data-qa='signup-button']").click()

    # Wait a bit
    time.sleep(2)

    # เช็คข้อความ
    assert "Enter Account Information" in driver.page_source
    
    # คลิกเลือก Title (เช่น Mr.)
    driver.find_element(By.ID, "id_gender1").click()

    # กรอกรหัสผ่าน
    driver.find_element(By.ID, "password").send_keys(signup_data["password"])

    # เลือกวันเกิด
    driver.find_element(By.NAME, "days").send_keys("1")
    driver.find_element(By.NAME, "months").send_keys("January")
    driver.find_element(By.NAME, "years").send_keys("2000")

    # ติ๊ก newsletter
    driver.find_element(By.ID, "newsletter").click()

    # กรอกที่อยู่
    driver.find_element(By.ID, "first_name").send_keys("TestFirst")
    driver.find_element(By.ID, "last_name").send_keys("TestLast")
    driver.find_element(By.ID, "address1").send_keys("123 Test Street")

    # เลือกประเทศ
    driver.find_element(By.ID, "country").send_keys("United States")

    # กรอก State, City, Zipcode, Mobile Number
    driver.find_element(By.ID, "state").send_keys("California")
    driver.find_element(By.ID, "city").send_keys("Los Angeles")
    driver.find_element(By.ID, "zipcode").send_keys("90001")
    driver.find_element(By.ID, "mobile_number").send_keys("1234567890")

    # กดปุ่ม 'Create Account'
    driver.find_element(By.XPATH, "//button[@data-qa='create-account']").click()

    # เช็คว่าแสดงข้อความ 'Account Created!'
    assert "Account Created!" in driver.page_source

    signup_data = generate_signup_data()

    driver.quit()