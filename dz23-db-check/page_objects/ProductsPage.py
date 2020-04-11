from selenium.webdriver.common.by import By
from .BasePage import BasePage
from .ProductDetailsPage import ProductDetailsPage
from selenium.common.exceptions import NoSuchElementException
import allure


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

    @allure.step("Table with products is displayed")
    def __init__(self, driver):
        super().__init__(driver)
        self._wait(ProductsPage.PRODUCT_TABLE)
        self.productDetailsPage = ProductDetailsPage(driver)

    def __filter(self, name):
        with allure.step("Filtering products by {0} name".format(name)):
            self.logger.info("Filtering products by {0} name".format(name))
            self._input(self.PRODUCT_NAME_INPUT, name)
            self._click(self.FILTER_BUTTON)
            self.wait.until(lambda wd: wd.execute_script("return document.readyState") == "complete")

    @allure.step("Adding new product")
    def add_new_product(self, name, tag, model, image):
        self.logger.info("Adding new product")
        self.__filter(name)
        self._click(self.ADD_NEW_PRODUCT_BUTTON)
        self.productDetailsPage. \
            update_product_name(name). \
            update_product_model(model). \
            update_product_tag(tag). \
            update_product_image(image). \
            save()
        self._wait(self.ALERT_SUCCESS)

    def update_product_model(self, name, model):
        with allure.step("Update model for {0} product with new value {1}".format(name, model)):
            self.logger.info("Updating product model")
            self.__filter(name)
            self._click(self.CHECKBOX_ALL)
            self._click(self.EDIT_PRODUCT_BUTTON)
            self.productDetailsPage. \
                update_product_model(model). \
                save()
            self._wait(self.ALERT_SUCCESS)

    def delete_product_by_name(self, name):
        with allure.step("Delete product {0}".format(name)):
            self.logger.info("Deleting product by name {0}".format(name))
            self.__filter(name)
            self._click(self.CHECKBOX_ALL)
            self._click(self.DELETE_BUTTON)
            self.driver.switch_to.alert.accept()
            self._wait(self.ALERT_SUCCESS)

    def is_product_present(self, name):
        with allure.step("Verify if product {0} is present in the system".format(name)):
            self.__filter(name)
            if len(self.driver.find_elements(*self.NO_RESULT_TEXT)) == 0:
                return True
            return False

    def get_product_model(self, name):
        with allure.step("Obtain model of product {0}".format(name)):
            self.logger.info("Requesting model by product name {0}".format(name))
            if not self.is_product_present(name):
                raise NoSuchElementException("Product {0} is not present".format(name))
            return self._element(self.PRODUCT_MODEL).text
