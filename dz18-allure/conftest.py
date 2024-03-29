from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
import allure
import logging
import pytest


def pytest_addoption(parser):
    parser.addoption("--file", action="store", default="", help="Specify file to store Webdriver logs")
    parser.addoption("--browser-console-error", action="store_true", help="Collect browser console errors")


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
        screen_shot_name = "screenshot/ERR-{0}.png".format(datetime.now().strftime("%d-%b-%Y %H:%M:%S"))
        driver.save_screenshot(screen_shot_name)


def browser_console_error_check(driver):
    error_list = []
    b = driver.get_log("browser")
    for l in b:
        if l['level'] == "SEVERE":
            error_list.append(l)
    driver.close()
    assert not error_list, "There are browser errors during the test execution:\n {0}".format(error_list)


def allure_attach_screenshot(driver):
    allure.attach(
        body=driver.get_screenshot_as_png(),
        name="Screenshot",
        attachment_type=allure.attachment_type.PNG
    )


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
        allure_attach_screenshot(driver)
        if request.config.getoption("--browser-console-error"):
            browser_console_error_check(driver)
        else:
            driver.close()
    request.addfinalizer(teardown)
    return driver
