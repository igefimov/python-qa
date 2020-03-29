from selenium.webdriver.common.by import By
from .BasePage import BasePage


class AdminLoginPage(BasePage):
    OPENCART_ADMIN_URL = "http://192.168.0.122/opencart/admin/"
    USERNAME = "admin"
    PASSWORD = "admin"
    # OPENCART_ADMIN_URL = "https://demo.opencart.com/admin"
    # USERNAME = "demo"
    # PASSWORD = "demo"
    USERNAME_INPUT = (By.CSS_SELECTOR, "#input-username")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".btn-primary")
    FORGOTTEN_PASSWORD_LINK = (By.LINK_TEXT, "Forgotten Password")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(self.OPENCART_ADMIN_URL)
    
    def login(self):
        self.logger.info("Logging into the Admin section")
        self._input(self.USERNAME_INPUT, self.USERNAME)
        self._input(self.PASSWORD_INPUT, self.PASSWORD)
        self._click(self.LOGIN_BUTTON)

    def navigate_to_products(self):
        raise NotImplementedError("This method is not implemented")
