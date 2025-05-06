from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException

class ContactUsPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://automationexercise.com/contact_us"

    def open(self):
        self.driver.get(self.url)

    def fill_name(self, name):
        self.driver.find_element(By.NAME, "name").send_keys(name)

    def fill_email(self, email):
        self.driver.find_element(By.NAME, "email").send_keys(email)

    def fill_subject(self, subject):
        self.driver.find_element(By.NAME, "subject").send_keys(subject)

    def fill_message(self, message):
        self.driver.find_element(By.ID, "message").send_keys(message)

    def upload_file(self, filepath):
        self.driver.find_element(By.NAME, "upload_file").send_keys(filepath)

    def click_submit(self):
        self.driver.find_element(By.NAME, "submit").click()
        self.driver.switch_to.alert.accept()
    def click_submit_safe(self):
        self.driver.find_element(By.NAME, "submit").click()
        try:
            self.driver.switch_to.alert.accept()
        except NoAlertPresentException:
            pass

    def get_success_message(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".status.alert-success"))
        ).text
