from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from .BasePage import BasePage


class SecurityNotification(BasePage):
    SECURITY_NOTIFICATION = (By.CSS_SELECTOR, ".close")

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(self.driver, 5)

    def close(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.SECURITY_NOTIFICATION)).click()
        except TimeoutException:
            pass
