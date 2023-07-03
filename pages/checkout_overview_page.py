from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutOverviewPage():
    def __init__(self, driver):
        self.selenium_driver = driver
        self.wait = WebDriverWait(driver, timeout=60)

    def is_at(self):
        checkout_overview_title_heading = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "title")))
        if checkout_overview_title_heading.text == "Checkout: Overview":
            return True
        else:
            return False
    
    def is_product_selected(self, product_name):
        product_selected = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='inventory_item_name' and contains(.,'" + product_name + "')]")))
        if product_selected.is_displayed() == True:
            return True
        else:
            return False
    
    def finish(self):
        self.wait.until(EC.visibility_of_element_located((By.ID, "finish"))).click()