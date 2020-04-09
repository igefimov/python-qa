from selenium.webdriver.common.by import By
from .BasePage import BasePage
import allure


class DashBoardPage(BasePage):
    DASHBOARD_HEADER = (By.CSS_SELECTOR, "#content div > h1")
    driver = None
    wait = None

    @allure.step("Dashboard header is present")
    def __init__(self, driver):
        super().__init__(driver)
        self._element(self.DASHBOARD_HEADER)
