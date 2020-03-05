import pytest
from selenium import webdriver
from locators import CommonElements


def pytest_addoption(parser):
    parser.addoption("--implicit-wait", action="store", default="", help="Provide value in seconds")


@pytest.fixture
def chrome(request):
    driver = webdriver.Chrome()
    timeout = request.config.getoption("--implicit-wait")
    if timeout != "":
        driver.implicitly_wait(timeout)
    driver.maximize_window()
    driver.get(CommonElements.OPENCART_URL)

    def teardown():
        driver.close()
    request.addfinalizer(teardown)
    return driver
