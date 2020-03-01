import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as OptionsChrome
from selenium.webdriver.firefox.options import Options as OptionsFirefox


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="Chrome", help="Specify browser: Chrome or Firefox")
    parser.addoption("--headless", action="store_true", default="False", help="Specify browser: Chrome or Firefox")
    parser.addoption("--url", action="store", default="http://192.168.0.122/opencart", help="Specify browser: Chrome or Firefox")

@pytest.fixture
def cmdopt(request):
    browser = request.config.getoption("--browser")
    if browser.upper() == 'CHROME':
        chrome_options = OptionsChrome()
        chrome_options.add_argument("--kiosk")
        if request.config.getoption("--headless") is True:
            chrome_options.add_argument("--headless")
        return webdriver.Chrome(options=chrome_options), request.config.getoption("--url")
    elif browser.upper() == "FIREFOX":
        firefox_options = OptionsFirefox()
        firefox_options.add_argument("--start-maximized")
        if request.config.getoption("--headless") is True:
            firefox_options.headless = True
        return webdriver.Firefox(options=firefox_options), request.config.getoption("--url")

    def teardown():
        browser.close()
    request.addfinalizer(teardown)
