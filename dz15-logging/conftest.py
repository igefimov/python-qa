from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
import logging
import pytest

logging.basicConfig(
    filename="log/test.log",
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
    logger.info("===================== Launching browser =====================")
    driver = EventFiringWebDriver(webdriver.Chrome(), MyListener())
    driver.maximize_window()

    def teardown():
        driver.save_screenshot("screenshot/OK-{0}.png".format(datetime.now().strftime("%d-%b-%Y %H:%M:%S")))
        driver.close()

    request.addfinalizer(teardown)
    return driver
