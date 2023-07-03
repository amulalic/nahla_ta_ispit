from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductsPage():
    def __init__(self, driver):
        self.selenium_driver = driver
        self.wait = WebDriverWait(driver, timeout=60)

    def is_at(self):
        products_title_heading = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "title")))
        if products_title_heading.text == "Products":
            return True
        else:
            return False
    
    def add_product(self, product_name):
        add_to_cart_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(.,'" + product_name + "')]/parent::div/parent::div[@class='inventory_item_description']//button[text()='Add to cart']")))
        add_to_cart_button.click()
    
    def log_out(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, "react-burger-menu-btn"))).click()
        self.wait.until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))).click()