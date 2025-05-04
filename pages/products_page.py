from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class ProductsPage:
    def __init__(self, driver):
        self.driver = driver
    #TC01
    products_button = (By.XPATH, "//a[@href='/products']")
    product_items = (By.CSS_SELECTOR, ".features_items .product-image-wrapper")

    def go_to_products_page(self):
        self.driver.find_element(*self.products_button).click()

    def get_all_products(self):
        return self.driver.find_elements(*self.product_items)
    
    #TC02
    product_names = (By.CSS_SELECTOR, ".productinfo.text-center p")
    product_prices = (By.CSS_SELECTOR, ".productinfo.text-center h2")
    add_to_cart_buttons = (By.CSS_SELECTOR, ".product-overlay .add-to-cart")

    def get_product_names(self):
        return self.driver.find_elements(*self.product_names)

    def get_product_prices(self):
        return self.driver.find_elements(*self.product_prices)

    def get_add_to_cart_buttons(self):
        return self.driver.find_elements(*self.add_to_cart_buttons)
    
    product_cards = (By.CSS_SELECTOR, ".product-image-wrapper")
    add_to_cart_overlay_buttons = (By.CSS_SELECTOR, ".product-overlay .add-to-cart")

    def hover_over_product(self, index):
        product_elements = self.driver.find_elements(*self.product_cards)
        hover_element = product_elements[index]
        ActionChains(self.driver).move_to_element(hover_element).perform()

    def get_add_to_cart_overlay_buttons(self):
        return self.driver.find_elements(*self.add_to_cart_overlay_buttons)
    
    #TC03
    view_product_buttons = (By.XPATH, "//a[text()='View Product']")

    def click_view_product_by_index(self, index=0):
        buttons = self.driver.find_elements(*self.view_product_buttons)
        buttons[index].click()