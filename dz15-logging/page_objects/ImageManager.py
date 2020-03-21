from js.onClick import ON_CLICK_JS_EVENT
from .BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os


class ImageManager(BasePage):
    UPLOAD_INPUT = (By.CSS_SELECTOR, "#form-upload > input[type=file]")
    IMAGES_TEXT = (By.CSS_SELECTOR, "#filemanager .col-sm-3")
    IMAGES = (By.CSS_SELECTOR, "#filemanager img")

    def __init__(self, driver):
        super().__init__(driver)

    def upload_image(self, image):
        os.chdir('dz14/img')
        filename = os.path.join(os.getcwd(), image)
        self.driver.execute_script(ON_CLICK_JS_EVENT.format(token=self.get_user_token))

        input_manager = self.driver.find_element_by_css_selector("#form-upload > input[type=file]")
        input_manager.send_keys(filename)
        self._wait_alert_is_present()
        self.driver.switch_to.alert.accept()
        self.wait.until(EC.element_to_be_clickable(self.IMAGES))
        elements = self._elements(self.IMAGES_TEXT)
        for i in elements:
            if i.text == image:
                i.click()
                break
