from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutCompletePage():
    def __init__(self, driver):
        self.selenium_driver = driver
        self.wait = WebDriverWait(driver, timeout=60)

    def is_at(self):
        checkout_complete_title_heading = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "title")))
        if checkout_complete_title_heading.text == "Checkout: Complete!":
            return True
        else:
            return False