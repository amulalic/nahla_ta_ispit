from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class YourCartPage():
    def __init__(self, driver):
        self.selenium_driver = driver
        self.wait = WebDriverWait(driver, timeout=60)
    
    def go_to(self):
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))).click()

    def is_at(self):
        your_cart_title_heading = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "title")))
        if your_cart_title_heading.text == "Your Cart":
            return True
        else:
            return False
    
    def is_product_in_cart(self, product_name):
        product_in_cart = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='inventory_item_name' and contains(.,'" + product_name + "')]")))
        if product_in_cart.is_displayed() == True:
            return True
        else:
            return False
    
    def checkout(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()