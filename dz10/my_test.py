from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import CommonElements
from locators import MainPage
from locators import ProductPage


def test_02_product_page(chrome):
    wait = WebDriverWait(chrome, 5)
    # Click on 3rd featured product
    feature_section_element = chrome.find_element(*MainPage.FEATURED_SECTION)
    feature_section_element.find_elements_by_class_name("image")[2].click()
    wait.until(EC.staleness_of(feature_section_element))
    wait.until(EC.presence_of_element_located(ProductPage.MAIN_IMAGE))
    try:
        wait.until(EC.presence_of_element_located(CommonElements.SEARCH_INPUT))
        wait.until(EC.presence_of_element_located(CommonElements.SEARCH_BUTTON))
        wait.until(EC.visibility_of_element_located(ProductPage.PRODUCT_NAME))
        wait.until(EC.visibility_of_element_located(ProductPage.QUANTITY_INPUT))
        wait.until(EC.visibility_of_element_located(ProductPage.ADD_TO_CART_BUTTON))
    except NoSuchElementException as e:
        print("My error handler:" + e.msg)
    finally:
        print("Fixture will close the browser")
