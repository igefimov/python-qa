from locators import CommonElements
from locators import MainPage

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

def test_main_page():
    driver = webdriver.Chrome()
    driver.get("http://192.168.0.122/opencart")
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

def test_product_page():
    driver = webdriver.Chrome()
    driver.get("http://192.168.0.122/opencart")

    #Click on 3rd featured product
    driver.find_element(*MainPage.FEATURED_SECTION).find_elements_by_class_name("image")[2].click()
    try:
        driver.find_element(*CommonElements.SEARCH_INPUT)
        driver.find_element(*CommonElements.SEARCH_BUTTON)
    except NoSuchElementException as e:
        print("My error handler:" + e.msg)

    finally:
        driver.close()
