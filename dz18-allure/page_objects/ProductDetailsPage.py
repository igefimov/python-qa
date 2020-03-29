from selenium.webdriver.common.by import By
from .BasePage import BasePage
from .ImageManager import ImageManager
import allure


class ProductDetailsPage(BasePage):
    PRODUCT_NAME_INPUT = (By.CSS_SELECTOR, "#input-name1")
    META_TITLE_INPUT = (By.CSS_SELECTOR, "#input-meta-title1")
    DATA_TAB = (By.CSS_SELECTOR, "#form-product li:nth-child(2)")
    GENERAL_TAB = (By.CSS_SELECTOR, "#form-product li:nth-child(1)")
    IMAGE_TAB = (By.LINK_TEXT, "Image")
    MODEL_INPUT = (By.CSS_SELECTOR, "#input-model")
    SAVE_BUTTON = (By.CSS_SELECTOR, ".btn-primary")
    ALERT_SUCCESS = (By.CSS_SELECTOR, ".alert-success")
    PRODUCT_IMAGE = (By.CSS_SELECTOR, "#thumb-image")
    CHANGE_IMAGE_BUTTON = (By.CSS_SELECTOR, "#button-image")

    def __init__(self, driver):
        super().__init__(driver)

    def update_product_name(self, value):
        with allure.step("Updating products name with a new value {0}".format(value)):
            self.logger.info("Updating name for current product")
            self._input(self.PRODUCT_NAME_INPUT, value)
            return self

    def update_product_model(self, value):
        with allure.step("Updating products model with a new value {0}".format(value)):
            self.logger.info("Updating model for current product")
            self._click(self.DATA_TAB)
            self._input(self.MODEL_INPUT, value)
            self._click(self.GENERAL_TAB)
            return self

    def update_product_tag(self, value):
        with allure.step("Updating products tag with a new value {0}".format(value)):
            self.logger.info("Updating tag for current product")
            self._input(self.META_TITLE_INPUT, value)
            return self

    def update_product_image(self, value):
        with allure.step("Updating products image with a new value {0}".format(value)):
            self.logger.info("Updating image for current product")
            self._click(self.IMAGE_TAB)
            self.__upload_image(value)
            return self

    # def update_field(self, field, value):
    #     with allure.step("Updating field {0} with value {1}".format(field, value)):
    #         self.logger.info("Updating {0} field for current product".format(field))
    #         if field == "name":
    #             self._input(self.PRODUCT_NAME_INPUT, value)
    #             return self
    #         if field == "model":
    #             self._click(self.DATA_TAB)
    #             self._input(self.MODEL_INPUT, value)
    #             self._click(self.GENERAL_TAB)
    #             return self
    #         if field == "tag":
    #             self._input(self.META_TITLE_INPUT, value)
    #             return self
    #         if field == "image":
    #             self._click(self.IMAGE_TAB)
    #             self.__upload_image(value)
    #             return self

    @allure.step("Saving")
    def save(self):
        self._click(self.SAVE_BUTTON)

    def __upload_image(self, image):
        with allure.step("Uploading image {0}".format(image)):
            self._click(self.PRODUCT_IMAGE)
            self._click(self.CHANGE_IMAGE_BUTTON)
            ImageManager(self.driver).upload_image(image)
