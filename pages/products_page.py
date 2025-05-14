from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class ProductsPage:
    def __init__(self, driver):
        self.driver = driver
    #TC08
    products_button = (By.XPATH, "//a[@href='/products']")
    product_items = (By.CSS_SELECTOR, ".features_items .product-image-wrapper")

    def go_to_products_page(self):
        self.driver.find_element(*self.products_button).click()

    def get_all_products(self):
        return self.driver.find_elements(*self.product_items)
    
    #TC09
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
    
    #TC10
    view_product_buttons = (By.XPATH, "//a[text()='View Product']")

    def click_view_product_by_index(self, index=0):
        buttons = self.driver.find_elements(*self.view_product_buttons)
        buttons[index].click()

    #TC11
    search_input = (By.ID, "search_product")
    search_button = (By.ID, "submit_search")
    searched_products = (By.CSS_SELECTOR, ".features_items .productinfo.text-center p")

    def search_product(self, keyword):
        self.driver.find_element(*self.search_input).send_keys(keyword)
        self.driver.find_element(*self.search_button).click()

    def get_search_results_names(self):
        return self.driver.find_elements(*self.searched_products)
    
    # TC12
    women_tops_category = (By.XPATH, "//a[@href='#Women']")
    women_tops_subcategory = (By.XPATH, "//a[text()='Tops ']")

    category_products = (By.CSS_SELECTOR, ".features_items .productinfo.text-center p")

    def click_category_women_tops(self):
        self.driver.find_element(*self.women_tops_category).click()
        time.sleep(1)
        self.driver.find_element(*self.women_tops_subcategory).click()
        time.sleep(1)

    def get_category_products_names(self):
        return self.driver.find_elements(*self.category_products)
    
    # TC13
    add_to_cart_buttons = (By.XPATH, "//div[@class='product-overlay']//a[contains(text(),'Add to cart')]")
    product_boxes = (By.CLASS_NAME, "product-image-wrapper")

    modal_popup = (By.ID, "cartModal")
    modal_visible = (By.XPATH, "//div[@id='cartModal'][@style='display: block;']")

    continue_btn = (By.XPATH, "//button[contains(text(),'Continue Shopping')]")
    view_cart_btn = (By.XPATH, "//u[contains(text(),'View Cart')]")

    def hover_and_add_first_product_to_cart(self):
        actions = ActionChains(self.driver)
        product = self.driver.find_elements(*self.product_boxes)[0]
        actions.move_to_element(product).perform()

        add_buttons = self.driver.find_elements(*self.add_to_cart_buttons)
        assert add_buttons, "No 'Add to cart' buttons found"
        add_buttons[0].click()

    def is_add_to_cart_modal_visible(self):
        wait = WebDriverWait(self.driver, 10)
        modal = wait.until(EC.visibility_of_element_located((By.ID, "cartModal")))
        return modal.is_displayed()

    def close_cart_modal(self):
        self.driver.find_element(*self.continue_btn).click()
    
    #TC14
    def get_current_product_names(self):
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".productinfo.text-center p")
        return [el.text.strip() for el in elements]

    def click_next_page(self):
        pagination_links = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".pagination li a"))
        )
        for link in pagination_links:
            print("Pagination link:", link.text.strip())
            if link.text.strip() == '>':
                link.click()
                return
        raise Exception("Next page button (>) not found")
    
    #TC15
    def click_category_women_tops(self):
        women_category = self.driver.find_element(By.XPATH, "//a[@href='#Women']")
        women_category.click()
        time.sleep(1)

        tops_link = self.driver.find_element(By.XPATH, "//a[contains(text(), 'Tops')]")
        tops_link.click()

    def search_product(self, keyword):
        search_input = self.driver.find_element(By.ID, "search_product")
        search_input.clear()
        search_input.send_keys(keyword)
        self.driver.find_element(By.ID, "submit_search").click()

    def get_search_results_names(self):
        return self.driver.find_elements(By.CSS_SELECTOR, ".productinfo.text-center p")
