from page_objects.AdminLoginPage import AdminLoginPage
from page_objects.DashBoardPage import DashBoardPage
from page_objects.SecurityNotification import SecurityNotification
from page_objects.ProductsPage import ProductsPage
import allure

PRODUCT_NAME = "Test_product"
PRODUCT_TAG = "Test_tag"
PRODUCT_MODEL = "Test_model"
PRODUCT_MODEL_NEW = "Test new model"
PRODUCT_IMAGE = 'jb.jpg'


@allure.title("Add new product {0} to the system".format(PRODUCT_NAME))
@allure.tag("adminSection", "add")
@allure.severity(allure.severity_level.CRITICAL)
def test_01_add_new_product(browser):
    AdminLoginPage(browser).login()
    SecurityNotification(browser).close()
    DashBoardPage(browser).navigate_to_products()
    ProductsPage(browser).add_new_product(PRODUCT_NAME, PRODUCT_TAG, PRODUCT_MODEL, PRODUCT_IMAGE)
    assert ProductsPage(browser).is_product_present(PRODUCT_NAME) is True, "{0} was added successfully".format(
        PRODUCT_NAME)


@allure.title("Update products {0} model".format(PRODUCT_NAME))
@allure.tag("adminSection", "update")
@allure.severity(allure.severity_level.NORMAL)
def test_02_update_product_model(browser):
    AdminLoginPage(browser).login()
    SecurityNotification(browser).close()
    DashBoardPage(browser).navigate_to_products()
    ProductsPage(browser).update_product_model(PRODUCT_NAME, PRODUCT_MODEL_NEW)
    assert ProductsPage(browser).get_product_model(
        PRODUCT_NAME) == PRODUCT_MODEL_NEW, "{0} was updated successfully".format(PRODUCT_NAME)


@allure.title("Remove product {0} from the system".format(PRODUCT_NAME))
@allure.tag("adminSection", "delete")
@allure.severity(allure.severity_level.CRITICAL)
def test_03_remove_product_by_its_name(browser):
    AdminLoginPage(browser).login()
    SecurityNotification(browser).close()
    DashBoardPage(browser).navigate_to_products()
    ProductsPage(browser).delete_product_by_name(PRODUCT_NAME)
    assert ProductsPage(browser).is_product_present(PRODUCT_NAME) is False, "{0} was removed successfully".format(
        PRODUCT_NAME)
