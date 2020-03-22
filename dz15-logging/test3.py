from page_objects.AdminLoginPage import AdminLoginPage
from page_objects.DashBoardPage import DashBoardPage
from page_objects.SecurityNotification import SecurityNotification
from page_objects.ProductsPage import ProductsPage

PRODUCT_NAME = "Test_product"
PRODUCT_TAG = "Test_tag"
PRODUCT_MODEL = "Test_model"
PRODUCT_MODEL_NEW = "Test new model"
PRODUCT_IMAGE = 'jb.jpg'


def browser_console_error_check(driver):
    error_list = []
    b = driver.get_log("browser")
    for l in b:
        if l['level'] == "SEVERE":
            error_list.append(l)
    assert not error_list, "There are browser errors during the test execution:\n {0}".format(error_list)


def test_01_add_new_product(browser):
    AdminLoginPage(browser).login()
    SecurityNotification(browser).close()
    DashBoardPage(browser).navigate_to_products()
    ProductsPage(browser).add_new_product(PRODUCT_NAME, PRODUCT_TAG, PRODUCT_MODEL, PRODUCT_IMAGE)
    assert ProductsPage(browser).is_product_present(PRODUCT_NAME) is True, "{0} was added successfully".format(PRODUCT_NAME)
    browser_console_error_check(browser)


def test_02_update_product_model(browser):
    AdminLoginPage(browser).login()
    SecurityNotification(browser).close()
    DashBoardPage(browser).navigate_to_products()
    ProductsPage(browser).update_product_model(PRODUCT_NAME, PRODUCT_MODEL_NEW)
    assert ProductsPage(browser).get_product_model(PRODUCT_NAME) == PRODUCT_MODEL_NEW, "{0} was updated successfully".format(PRODUCT_NAME)
    browser_console_error_check(browser)


def test_03_remove_product_by_its_name(browser):
    AdminLoginPage(browser).login()
    SecurityNotification(browser).close()
    DashBoardPage(browser).navigate_to_products()
    ProductsPage(browser).delete_product_by_name(PRODUCT_NAME)
    assert ProductsPage(browser).is_product_present(PRODUCT_NAME) is False, "{0} was removed successfully".format(PRODUCT_NAME)
    browser_console_error_check(browser)
