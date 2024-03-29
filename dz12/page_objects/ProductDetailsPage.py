from selenium.webdriver.common.by import By
from .BasePage import BasePage


class ProductDetailsPage(BasePage):
    PRODUCT_NAME_INPUT = (By.CSS_SELECTOR, "#input-name1")
    META_TITLE_INPUT = (By.CSS_SELECTOR, "#input-meta-title1")
    DATA_TAB = (By.CSS_SELECTOR, "#form-product li:nth-child(2)")
    GENERAL_TAB = (By.CSS_SELECTOR, "#form-product li:nth-child(1)")
    MODEL_INPUT = (By.CSS_SELECTOR, "#input-model")
    SAVE_BUTTON = (By.CSS_SELECTOR, ".btn-primary")
    ALERT_SUCCESS = (By.CSS_SELECTOR, ".alert-success")

    def __init__(self, driver):
        super().__init__(driver)

    def update_field(self, field, value):
        if field == "name":
            self._input(self.PRODUCT_NAME_INPUT, value)
            return self
        if field == "model":
            self._click(self.DATA_TAB)
            self._input(self.MODEL_INPUT, value)
            self._click(self.GENERAL_TAB)
            return self
        if field == "tag":
            self._input(self.META_TITLE_INPUT, value)
            return self

    def save(self):
        self._click(self.SAVE_BUTTON)
