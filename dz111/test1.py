from .locators import ProductsPage
from .locators import ProductDetailsPage
from selenium.webdriver.support import expected_conditions as EC


PRODUCT_NAME = "Test_product"
PRODUCT_TAG = "Test_tag"
PRODUCT_MODEL = "Test_model"


def test_01_add_new_product(chrome):
    driver, wait = chrome
    driver.find_element(*ProductsPage.ADD_NEW_PRODUCT_BUTTON).click()
    driver.find_element(*ProductDetailsPage.PRODUCT_NAME_INPUT).send_keys(PRODUCT_NAME)
    driver.find_element(*ProductDetailsPage.META_TITLE_INPUT).send_keys(PRODUCT_TAG)
    driver.find_element(*ProductDetailsPage.DATA_TAB).click()
    driver.find_element(*ProductDetailsPage.MODEL_INPUT).send_keys(PRODUCT_MODEL)
    driver.find_element(*ProductDetailsPage.SAVE_BUTTON).click()
    wait.until(EC.visibility_of_element_located(ProductDetailsPage.ALERT_SUCCESS))


def test_02_update_product_tag(chrome):
    driver, wait = chrome
    driver.find_element(*ProductsPage.PRODUCT_NAME_INPUT).send_keys(PRODUCT_NAME)
    driver.find_element(*ProductsPage.FILTER_BUTTON).click()
    wait.until(lambda wd: wd.execute_script("return document.readyState") == "complete")
    driver.find_element(*ProductsPage.CHECKBOX_ALL).click()
    driver.find_element(*ProductsPage.EDIT_PRODUCT_BUTTON).click()
    product_tag = driver.find_element(*ProductDetailsPage.META_TITLE_INPUT)
    product_tag.clear()
    product_tag.send_keys(PRODUCT_TAG)
    driver.find_element(*ProductDetailsPage.SAVE_BUTTON).click()
    wait.until(EC.visibility_of_element_located(ProductDetailsPage.ALERT_SUCCESS))


def test_03_remove_product_by_its_name(chrome):
    driver, wait = chrome
    driver.find_element(*ProductsPage.PRODUCT_NAME_INPUT).send_keys(PRODUCT_NAME)
    driver.find_element(*ProductsPage.FILTER_BUTTON).click()
    wait.until(lambda wd: wd.execute_script("return document.readyState") == "complete")
    driver.find_element(*ProductsPage.CHECKBOX_ALL).click()
    driver.find_element(*ProductsPage.DELETE_BUTTON).click()
    driver.switch_to.alert.accept()
    wait.until(EC.visibility_of_element_located(ProductDetailsPage.ALERT_SUCCESS))
