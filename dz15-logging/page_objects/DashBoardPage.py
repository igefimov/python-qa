from selenium.webdriver.common.by import By
from .BasePage import BasePage


class DashBoardPage(BasePage):
    DASHBOARD_HEADER = (By.CSS_SELECTOR, "#content div > h1")
    driver = None
    wait = None

    def __init__(self, driver):
        super().__init__(driver)
        self._element(self.DASHBOARD_HEADER)
