from locators import AdminLoginPage
from locators import CatalogPage
from locators import CommonElements
from locators import MainPage
from locators import ProductPage
from locators import SearchResults

from selenium.common.exceptions import NoSuchElementException


def test_01_main_page(chrome):
    try:
        chrome.find_element(*CommonElements.SEARCH_INPUT)
        chrome.find_element(*CommonElements.SEARCH_BUTTON)
        chrome.find_element(*MainPage.BOTTOM_CAROUSEL)
        chrome.find_element(*MainPage.FEATURED_LABEL)
        chrome.find_element(*MainPage.FEATURED_SECTION)
    except NoSuchElementException as e:
        print("My error handler:" + e.msg)


def test_02_product_page(chrome):
    # Click on 3rd featured product
    chrome.find_element(*MainPage.FEATURED_SECTION).find_elements_by_class_name("image")[2].click()

    try:
        chrome.find_element(*CommonElements.SEARCH_INPUT)
        chrome.find_element(*CommonElements.SEARCH_BUTTON)
        chrome.find_element(*ProductPage.PRODUCT_NAME)
        chrome.find_element(*ProductPage.QUANTITY_INPUT)
        chrome.find_element(*ProductPage.ADD_TO_CART_BUTTON)
    except NoSuchElementException as e:
        print("My error handler:" + e.msg)


def test_03_mp3_catalog_page(chrome):
    chrome.get("{0}{1}".format(CommonElements.OPENCART_URL, "/index.php?route=product/category&path=34"))
    try:
        chrome.find_element(*CommonElements.SEARCH_INPUT)
        chrome.find_element(*CommonElements.SEARCH_BUTTON)
        chrome.find_element(*CatalogPage.LEFT_SELECTION_PANEL)
        chrome.find_element(*CatalogPage.SECTION_NAME)
        chrome.find_element(*CatalogPage.SECTION_IMAGE)
        chrome.find_element(*CatalogPage.SECTION_DESCRIPTION)

    except NoSuchElementException as e:
        print("My error handler:" + e.msg)


def test_04_admin_login_page(chrome):
    chrome.get("{0}{1}".format(CommonElements.OPENCART_URL, "/admin"))
    try:
        chrome.find_element(*AdminLoginPage.OPENCART_LOGO)
        chrome.find_element(*AdminLoginPage.USERNAME_INPUT)
        chrome.find_element(*AdminLoginPage.PASSWORD_INPUT)
        chrome.find_element(*AdminLoginPage.LOGIN_BUTTON)
        chrome.find_element(*AdminLoginPage.FORGOTTEN_PASSWORD_LINK)
    except NoSuchElementException as e:
        print("My error handler:" + e.msg)


def test_05_search_results_page(chrome):
    # Open search results
    chrome.find_element(*CommonElements.SEARCH_INPUT).send_keys("mac")
    chrome.find_element(*CommonElements.SEARCH_BUTTON).click()
    try:
        chrome.find_element(*CommonElements.SEARCH_INPUT)
        chrome.find_element(*CommonElements.SEARCH_BUTTON)
        chrome.find_element(*SearchResults.SEARCH_TOPIC)
        chrome.find_element(*SearchResults.SEARCH_CRITERIA_CATEGORY)
        chrome.find_element(*SearchResults.SEARCH_IN_PRODUCT_DESCRIPTION)
        chrome.find_element(*SearchResults.SEARCH_IN_SUBCATEGORIES)
        chrome.find_element(*SearchResults.SEARCH_BUTTON)
    except NoSuchElementException as e:
        print("My error handler:" + e.msg)
