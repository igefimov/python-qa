from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    LEFT_MENU_CATALOG = (By.CSS_SELECTOR, "#menu-catalog")
    LEFT_MENU_CATALOG_CATEGORY = (By.CSS_SELECTOR, "#collapse1 > li")
    LEFT_MENU_CATALOG_LAST_CATEGORY = (By.CSS_SELECTOR, "#collapse1 > :nth-child(10)")
    ALERT_SUCCESS = (By.CSS_SELECTOR, ".alert-success")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

    def _click(self, element):
        self._element(element).click()

    def _element(self, locator):
        return self.driver.find_element(*locator)

    def _input(self, locator, value):
        element = self._element(locator)
        element.clear()
        element.send_keys(value)

    def _wait(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))

    def navigate_to_products(self):
        self._click(self.LEFT_MENU_CATALOG)
        self.wait.until(EC.visibility_of_element_located(self.LEFT_MENU_CATALOG_LAST_CATEGORY))
        catalog_categories = self.driver.find_elements(*self.LEFT_MENU_CATALOG_CATEGORY)
        for category in catalog_categories:
            if category.text == "Products":
                category.click()
                break
