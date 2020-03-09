import pytest

from .locators import AdminLoginPage, CommonElements, ProductsPage
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def navigate_to_products_page(driver):
    wait = WebDriverWait(driver, 5)
    driver.get(AdminLoginPage.OPENCART_ADMIN_URL)
    username = driver.find_element(*AdminLoginPage.USERNAME_INPUT)
    username.clear()
    username.send_keys(AdminLoginPage.USERNAME)
    password = driver.find_element(*AdminLoginPage.PASSWORD_INPUT)
    password.clear()
    password.send_keys(AdminLoginPage.PASSWORD)
    driver.find_element(*AdminLoginPage.LOGIN_BUTTON).click()
    try:
        wait.until(EC.visibility_of_element_located(CommonElements.SECURITY_NOTIFICATION)).click()
    except TimeoutException:
        pass
    driver.find_element(*CommonElements.LEFT_MENU_CATALOG).click()

    wait.until(EC.visibility_of_element_located(CommonElements.LEFT_MENU_CATALOG_LAST_CATEGORY))

    catalog_categories = driver.find_elements(*CommonElements.LEFT_MENU_CATALOG_CATEGORY)
    for category in catalog_categories:
        if category.text == "Products":
            category.click()
            break
    wait.until(EC.visibility_of_element_located(ProductsPage.PRODUCT_TABLE))
    return wait


def pytest_addoption(parser):
    parser.addoption("--implicit-wait", action="store", default="", help="Provide value in seconds")


@pytest.fixture
def chrome(request):
    driver = webdriver.Chrome()
    timeout = request.config.getoption("--implicit-wait")
    if timeout != "":
        driver.implicitly_wait(timeout)
    driver.maximize_window()
    driver.get(AdminLoginPage.OPENCART_ADMIN_URL)
    wait = navigate_to_products_page(driver)

    def teardown():
        driver.close()
    request.addfinalizer(teardown)
    return driver, wait
