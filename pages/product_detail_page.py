from selenium.webdriver.common.by import By

class ProductDetailPage:
    def __init__(self, driver):
        self.driver = driver

    product_name = (By.CSS_SELECTOR, ".product-information h2")

    def get_product_name(self):
        return self.driver.find_element(*self.product_name).text
