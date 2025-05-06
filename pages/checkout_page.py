from selenium.webdriver.common.by import By

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    # Locators
    product_summary_table = (By.ID, "cart_info")
    comment_textarea = (By.NAME, "message")
    place_order_button = (By.XPATH, "//a[contains(text(),'Place Order')]")

    # Actions
    def is_product_summary_displayed(self):
        return self.driver.find_element(*self.product_summary_table).is_displayed()

    def enter_comment(self, text):
        comment_box = self.driver.find_element(*self.comment_textarea)
        comment_box.clear()
        comment_box.send_keys(text)

    def click_place_order(self):
        self.driver.find_element(*self.place_order_button).click()
