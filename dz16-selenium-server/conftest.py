from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
import logging
import pytest


def pytest_addoption(parser):
    parser.addoption("--file", action="store", default="", help="Specify file to store Webdriver logs")
    parser.addoption("--browser", action="store", default="chrome", choices=["chrome", "firefox", "safari", "opera"])
    parser.addoption("--executor", action="store", default="192.168.0.123")
    parser.addoption("--headless", action="store_true", default="True", help="Specify browser: Chrome or Firefox")


logging.basicConfig(
    format='%(asctime)s %(name)s [%(levelname)s]: %(message)s',
    level=logging.INFO
)
logger = logging.getLogger('Driver')


class MyListener(AbstractEventListener):
    def after_navigate_to(self, url, driver):
        logger.info(f"I'm on {url}")

    def after_find(self, by, value, driver):
        logger.info(f"I've found '{value}' with '{by}'")

    def before_click(self, element, driver):
        logger.info(f"I'm clicking {element.text} {element.tag_name}")

    def before_execute_script(self, script, driver):
        logger.info(f"I'm executing '{script}'")

    def after_close(self, driver):
        logger.info(f"===================== Finita la comedia =====================")

    def on_exception(self, exception, driver):
        logger.error(f'Houston, we have a problem : {exception}')
        driver.save_screenshot("screenshot/ERR-{0}.png".format(datetime.now().strftime("%d-%b-%Y %H:%M:%S")))


@pytest.fixture
def browser(request):
    log_file = request.config.getoption("--file")
    if log_file:
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)
        logging.basicConfig(
            filename=log_file,
            format='%(asctime)s %(name)s [%(levelname)s]: %(message)s',
            level=logging.INFO
        )

    logger.info("===================== Launching browser =====================")
    desired_capabilities = DesiredCapabilities.CHROME
    options = webdriver.ChromeOptions()
    options.add_experimental_option('w3c', False)
    desired_capabilities['loggingPrefs'] = {'browser': 'ALL'}
    driver = EventFiringWebDriver(
        webdriver.Chrome(desired_capabilities=desired_capabilities, options=options),
        MyListener()
    )
    driver.maximize_window()

    def teardown():
        driver.close()

    request.addfinalizer(teardown)
    return driver


@pytest.fixture
def remote(request):
    browser = request.config.getoption("--browser")
    executor = request.config.getoption("--executor")
    options = None
    if browser == "chrome":
        options = webdriver.ChromeOptions()
    if browser == "firefox":
        options = webdriver.FirefoxOptions()
    if options is None:
        raise NotImplementedError("We don't support {0} browser at this moment".format(browser))
    if request.config.getoption("--headless"):
        options.add_argument("-headless")
        options.add_argument("--window-size=1600,1200")

    driver = webdriver.Remote(command_executor=f"http://{executor}:4444/wd/hub",
                              desired_capabilities={"browserName": browser},
                              options=options
                              )
    driver.maximize_window()
    request.addfinalizer(driver.quit)
    return driver


@pytest.fixture
def browserstack(request):
    desired_cap = {
        'browser': 'Chrome',
        'browser_version': '80.0',
        'os': 'Windows',
        'os_version': '10',
        'resolution': '1024x768',
        'name': 'Bstack-[Python] Sample Test'
    }

    driver = webdriver.Remote(
        command_executor='http://igorefimov1:XXXt@hub-cloud.browserstack.com/wd/hub',
        desired_capabilities=desired_cap)
    request.addfinalizer(driver.quit)
    return driver
