from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
import re
import logging


class BasePage:

    LEFT_MENU_CATALOG = (By.CSS_SELECTOR, "#menu-catalog")
    LEFT_MENU_CATALOG_CATEGORY = (By.CSS_SELECTOR, "#collapse1 > li")
    LEFT_MENU_CATALOG_LAST_CATEGORY = (By.CSS_SELECTOR, "#collapse1 > :nth-child(10)")
    ALERT_SUCCESS = (By.CSS_SELECTOR, ".alert-success")

    def __init__(self, driver):
        with allure.step("We are on the {0} page".format(self.__class__.__name__)):
            self.logger = logging.getLogger(self.__class__.__name__)
            self.logger.info("{0} initialized".format(self.__class__.__name__))
            self.driver = driver
            self.wait = WebDriverWait(self.driver, 5)

    def _click(self, element):
        with allure.step("Executing click on element: {0}".format(element)):
            self._element(element).click()

    def _element(self, locator):
        with allure.step("Searching for locator: {0}".format(locator)):
            return self.driver.find_element(*locator)

    def _elements(self, locator):
        with allure.step("Searching for locators: {0}".format(locator)):
            return self.driver.find_elements(*locator)

    def _input(self, locator, value):
        with allure.step("Typing {0} into locator {1}".format(value, locator)):
            element = self._element(locator)
            element.clear()
            element.send_keys(value)

    def _wait(self, locator):
        with allure.step("Waiting for locator {0} to be visible".format(locator)):
            self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Waiting for alert to be present")
    def _wait_alert_is_present(self):
            self.wait.until(EC.alert_is_present())

    @allure.step("Navigating to Products section")
    def navigate_to_products(self):
            self._click(self.LEFT_MENU_CATALOG)
            self.wait.until(EC.visibility_of_element_located(self.LEFT_MENU_CATALOG_LAST_CATEGORY))
            catalog_categories = self.driver.find_elements(*self.LEFT_MENU_CATALOG_CATEGORY)
            for category in catalog_categories:
                if category.text == "Products":
                    category.click()
                    break

    @property
    def get_user_token(self):
        return re.search(r'user_token=(\w+)&?', self.driver.current_url).group(1)
