from selenium.webdriver.common.by import By

class PaymentPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_name_on_card(self, name):
        self.driver.find_element(By.NAME, "name_on_card").send_keys(name)

    def enter_card_number(self, card_number):
        self.driver.find_element(By.NAME, "card_number").send_keys(card_number)

    def enter_cvc(self, cvc):
        self.driver.find_element(By.NAME, "cvc").send_keys(cvc)

    def enter_expiry_month(self, month):
        self.driver.find_element(By.NAME, "expiry_month").send_keys(month)

    def enter_expiry_year(self, year):
        self.driver.find_element(By.NAME, "expiry_year").send_keys(year)

    def click_pay_button(self):
        self.driver.find_element(By.ID, "submit").click()
