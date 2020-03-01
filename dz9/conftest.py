import pytest

from locators import CommonElements
from selenium import webdriver

@pytest.fixture
def chrome(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(CommonElements.OPENCART_URL)

    def teardown():
        driver.close()
    request.addfinalizer(teardown)
    return driver
