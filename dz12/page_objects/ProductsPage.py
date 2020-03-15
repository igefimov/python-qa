from selenium.webdriver.common.by import By
from .BasePage import BasePage
from .ProductDetailsPage import ProductDetailsPage
from selenium.common.exceptions import NoSuchElementException


class ProductsPage(BasePage):

    PRODUCT_TABLE = (By.CSS_SELECTOR, ".table-responsive")
    ADD_NEW_PRODUCT_BUTTON = (By.CSS_SELECTOR, ".btn-primary")
    PRODUCT_NAME_INPUT = (By.CSS_SELECTOR, "#input-name")
    FILTER_BUTTON = (By.CSS_SELECTOR, "#button-filter")
    CHECKBOX_ALL = (By.CSS_SELECTOR, "#form-product input[type=checkbox]")
    DELETE_BUTTON = (By.CSS_SELECTOR, ".btn-danger")
    EDIT_PRODUCT_BUTTON = (By.CSS_SELECTOR, "#form-product .btn-primary")
    NO_RESULT_TEXT = (By.XPATH, "//*[contains(text(), 'No results!')]")
    PRODUCT_MODEL = (By.CSS_SELECTOR, "#form-product table > tbody > tr > td:nth-child(4)")
    # ProductDetailsPage
    # PRODUCT_NAME_INPUT1 = (By.CSS_SELECTOR, "#input-name1")
    # META_TITLE_INPUT = (By.CSS_SELECTOR, "#input-meta-title1")
    # DATA_TAB = (By.CSS_SELECTOR, "#form-product li:nth-child(2)")
    # MODEL_INPUT = (By.CSS_SELECTOR, "#input-model")
    # SAVE_BUTTON = (By.CSS_SELECTOR, ".btn-primary")
    # ALERT_SUCCESS = (By.CSS_SELECTOR, ".alert-success")

    def __init__(self, driver):
        super().__init__(driver)
        self._wait(ProductsPage.PRODUCT_TABLE)
        self.productDetailsPage = ProductDetailsPage(driver)

    def __filter(self, name):
        self._input(self.PRODUCT_NAME_INPUT, name)
        self._click(self.FILTER_BUTTON)
        self.wait.until(lambda wd: wd.execute_script("return document.readyState") == "complete")

    def add_new_product(self, name, tag, model):
        self.__filter(name)
        self._click(self.ADD_NEW_PRODUCT_BUTTON)
        self.productDetailsPage.\
            update_field("name", name). \
            update_field("model", model). \
            update_field("tag", tag).\
            save()
        self._wait(self.ALERT_SUCCESS)

    def update_product_model(self, name, model):
        self.__filter(name)
        self._click(self.CHECKBOX_ALL)
        self._click(self.EDIT_PRODUCT_BUTTON)
        self.productDetailsPage.\
            update_field("model", model).\
            save()
        self._wait(self.ALERT_SUCCESS)

    def delete_product_by_name(self, name):
        self.__filter(name)
        self._click(self.CHECKBOX_ALL)
        self._click(self.DELETE_BUTTON)
        self.driver.switch_to.alert.accept()
        self._wait(self.ALERT_SUCCESS)

    def is_product_present(self, name):
        self.__filter(name)
        is_present = False
        try:
            self.driver.find_element(*self.NO_RESULT_TEXT)
        except NoSuchElementException:
            is_present = True
        finally:
            return is_present

    def get_product_model(self, name):
        if not self.is_product_present(name):
            raise NoSuchElementException("Product {0} is not present".format(name))
        return self._element(self.PRODUCT_MODEL).text
