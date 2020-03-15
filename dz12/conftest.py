import pytest
from selenium import webdriver


@pytest.fixture
def browser(request):
    driver = webdriver.Chrome()
    driver.maximize_window()

    def teardown():
        driver.close()
    request.addfinalizer(teardown)
    return driver
