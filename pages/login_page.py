from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.selenium_driver = driver
        self.wait = WebDriverWait(driver, timeout=60)
    
    def go_to(self):
        self.selenium_driver.get("https://www.saucedemo.com")
        self.selenium_driver.maximize_window()
    
    def is_at(self):
        checkout_complete_title_heading = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "login_logo")))
        if checkout_complete_title_heading.text == "Swag Labs":
            return True
        else:
            return False

    def login(self, username, password):
        username_field_locator = (By.ID, "user-name")
        wait_username_field = self.wait.until(EC.element_to_be_clickable(username_field_locator))
        wait_username_field.click()
        wait_username_field.clear()
        wait_username_field.send_keys(username)

        password_field = self.selenium_driver.find_element(By.ID, "password")
        password_field.click()
        password_field.clear()
        password_field.send_keys(password)

        login_button = self.selenium_driver.find_element(By.ID, "login-button")
        login_button.click()