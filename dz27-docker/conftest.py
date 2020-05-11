import pytest
from selenium import webdriver


@pytest.fixture
def browser(request):
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox");
    options.add_argument("--disable-dev-shm-usage");
    options.add_argument("--headless")
    options.add_argument("window-size=1920, 1080")
    driver = webdriver.Chrome(options=options)
    # driver.maximize_window()


    def teardown():
        driver.close()
    request.addfinalizer(teardown)
    return driver
