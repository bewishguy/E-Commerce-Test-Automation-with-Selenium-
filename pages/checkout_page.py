from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait   = WebDriverWait(driver, 10)

    # ── TC02
    def is_product_summary_displayed(self) -> bool:
        try:
            self.wait.until(EC.presence_of_element_located((By.ID, "cart_info")))
            return True
        except Exception as e:
            print(f"[ERROR] Product summary not found: {e}")
            return False

    # ── TC03
    def enter_comment(self, text):
        try:
            comment_box = self.wait.until(EC.visibility_of_element_located((By.NAME, "message")))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", comment_box)
            comment_box.clear()
            comment_box.send_keys(text)
            return True
        except Exception as e:
            print(f"[ERROR] Unable to enter comment: {e}")
            return False

    # ── TC04
    def click_place_order(self):
        try:
            place_order_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Place Order')]")))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", place_order_btn)
            place_order_btn.click()
            return True
        except Exception as e:
            print(f"[ERROR] Unable to click 'Place Order': {e}")
            return False
        
    # ── TC05   
    # def get_billing_address_text(self):
    #     return self.driver.find_element("xpath", "//ul[@id='address_invoice']").text

    # def get_delivery_address_text(self):
    #     return self.driver.find_element("xpath", "//ul[@id='address_delivery']").text
