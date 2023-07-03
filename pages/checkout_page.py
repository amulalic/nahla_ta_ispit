from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage():
    def __init__(self, driver):
        self.selenium_driver = driver
        self.wait = WebDriverWait(driver, timeout=60)

    def is_at(self):
        checkout_title_heading = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "title")))
        if checkout_title_heading.text == "Checkout: Your Information":
            return True
        else:
            return False
    
    def fill(self, first_name, last_name, zip_code):
        first_name_field = self.wait.until(EC.element_to_be_clickable((By.ID, "first-name")))
        first_name_field.click()
        first_name_field.clear()
        first_name_field.send_keys(first_name)

        last_name_field = self.selenium_driver.find_element(By.ID, "last-name")
        last_name_field.click()
        last_name_field.clear()
        last_name_field.send_keys(last_name)

        zip_code_field = self.selenium_driver.find_element(By.ID, "postal-code")
        zip_code_field.click()
        zip_code_field.clear()
        zip_code_field.send_keys(zip_code)
    
    def proceed(self):
        self.selenium_driver.find_element(By.ID, "continue").click()