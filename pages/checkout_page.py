from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait   = WebDriverWait(driver, 20)

    def is_product_summary_displayed(self) -> bool:
        try:
            self.wait.until(EC.presence_of_element_located((By.ID, "cart_info")))
            return True
        except Exception as e:
            print(f"[ERROR] Product summary not found: {e}")
            return False

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

    def click_place_order(self):
        try:
            place_order_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Place Order')]")))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", place_order_btn)
            place_order_btn.click()
            return True
        except Exception as e:
            print(f"[ERROR] Unable to click 'Place Order': {e}")
            return False
   
    def get_billing_address_text(self):
        billing_element = self.wait.until(
            EC.visibility_of_element_located((By.ID, "address_invoice"))
        )

        return billing_element.text.strip()

    def get_delivery_address_text(self):
        delivery_element = self.wait.until(
            EC.visibility_of_element_located((By.ID, "address_delivery"))
        )

        return delivery_element.text.strip()