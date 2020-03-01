#TODO подчеркиваются импорты красным и пишет Unresolved reference 'locators'
# Когда ставлю точку перед locators вот так:
# from locators import CommonElements
# больше не светится красным, но тест падает при запуске с ImportError: attempted relative import with no known parent package
from locators import AdminLoginPage
from locators import CatalogPage
from locators import CommonElements
from locators import MainPage
from locators import ProductPage
from locators import SearchResults

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


def test_01_main_page():
    driver = webdriver.Chrome()
    driver.get(CommonElements.OPENCART_URL)
    try:
        driver.find_element(*CommonElements.SEARCH_INPUT)
        driver.find_element(*CommonElements.SEARCH_BUTTON)
        driver.find_element(*MainPage.BOTTOM_CAROUSEL)
        driver.find_element(*MainPage.FEATURED_LABEL)
        driver.find_element(*MainPage.FEATURED_SECTION)
    except NoSuchElementException as e:
        print("My error handler:" + e.msg)
    finally:
        driver.close()


def test_02_product_page():
    driver = webdriver.Chrome()
    driver.get(CommonElements.OPENCART_URL)

    #Click on 3rd featured product
    driver.find_element(*MainPage.FEATURED_SECTION).find_elements_by_class_name("image")[2].click()

    try:
        driver.find_element(*CommonElements.SEARCH_INPUT)
        driver.find_element(*CommonElements.SEARCH_BUTTON)
        driver.find_element(*ProductPage.PRODUCT_NAME)
        driver.find_element(*ProductPage.QUANTITY_INPUT)
        driver.find_element(*ProductPage.ADD_TO_CART_BUTTON)
    except NoSuchElementException as e:
        print("My error handler:" + e.msg)

    finally:
        driver.close()


def test_03_mp3_catalog_page():
    driver = webdriver.Chrome()
    driver.get("{0}{1}".format(CommonElements.OPENCART_URL, "/index.php?route=product/category&path=34"))
    try:
        driver.find_element(*CommonElements.SEARCH_INPUT)
        driver.find_element(*CommonElements.SEARCH_BUTTON)
        driver.find_element(*CatalogPage.LEFT_SELECTION_PANEL)
        driver.find_element(*CatalogPage.SECTION_NAME)
        driver.find_element(*CatalogPage.SECTION_IMAGE)
        driver.find_element(*CatalogPage.SECTION_DESCRIPTION)

    except NoSuchElementException as e:
        print("My error handler:" + e.msg)
    finally:
        driver.close()


def test_04_admin_login_page():
    driver = webdriver.Chrome()
    driver.get("{0}{1}".format(CommonElements.OPENCART_URL, "/admin"))
    try:
        driver.find_element(*AdminLoginPage.OPENCART_LOGO)
        driver.find_element(*AdminLoginPage.USERNAME_INPUT)
        driver.find_element(*AdminLoginPage.PASSWORD_INPUT)
        driver.find_element(*AdminLoginPage.LOGIN_BUTTON)
        driver.find_element(*AdminLoginPage.FORGOTTEN_PASSWORD_LINK)
    except NoSuchElementException as e:
        print("My error handler:" + e.msg)
    finally:
        driver.close()

def test_05_search_results_page():
    driver = webdriver.Chrome()
    driver.get(CommonElements.OPENCART_URL)

    # Open search results
    driver.find_element(*CommonElements.SEARCH_INPUT).send_keys("mac")
    driver.find_element(*CommonElements.SEARCH_BUTTON).click()
    try:
        driver.find_element(*CommonElements.SEARCH_INPUT)
        driver.find_element(*CommonElements.SEARCH_BUTTON)
        driver.find_element(*SearchResults.SEARCH_TOPIC)
        driver.find_element(*SearchResults.SEARCH_CRITERIA_CATEGORY)
        driver.find_element(*SearchResults.SEARCH_IN_PRODUCT_DESCRIPTION)
        driver.find_element(*SearchResults.SEARCH_IN_SUBCATEGORIES)
        driver.find_element(*SearchResults.SEARCH_BUTTON)
    except NoSuchElementException as e:
        print("My error handler:" + e.msg)
    finally:
        driver.close()
