from page_objects.AdminLoginPage import AdminLoginPage
from page_objects.DashBoardPage import DashBoardPage
from page_objects.SecurityNotification import SecurityNotification
from page_objects.ProductsPage import ProductsPage
import allure
import config


@allure.title("Add new product {0} to the system".format(config.PRODUCT_NAME))
@allure.tag("adminSection", "add")
@allure.severity(allure.severity_level.CRITICAL)
def test_01_add_new_product(browser):
    AdminLoginPage(browser).login()
    SecurityNotification(browser).close()
    DashBoardPage(browser).navigate_to_products()
    ProductsPage(browser).add_new_product(config.PRODUCT_NAME, config.PRODUCT_TAG, config.PRODUCT_MODEL, config.PRODUCT_IMAGE)
    assert ProductsPage(browser).is_product_present(config.PRODUCT_NAME) is True, "{0} was added successfully".format(
        config.PRODUCT_NAME)


@allure.title("Update products {0} model".format(config.PRODUCT_NAME))
@allure.tag("adminSection", "update")
@allure.severity(allure.severity_level.NORMAL)
def test_02_update_product_model(browser):
    AdminLoginPage(browser).login()
    SecurityNotification(browser).close()
    DashBoardPage(browser).navigate_to_products()
    ProductsPage(browser).update_product_model(config.PRODUCT_NAME, config.PRODUCT_MODEL_NEW)
    assert ProductsPage(browser).get_product_model(
        config.PRODUCT_NAME) == config.PRODUCT_MODEL_NEW, "{0} was updated successfully".format(config.PRODUCT_NAME)


@allure.title("Remove product {0} from the system".format(config.PRODUCT_NAME))
@allure.tag("adminSection", "delete")
@allure.severity(allure.severity_level.CRITICAL)
def test_03_remove_product_by_its_name(browser):
    AdminLoginPage(browser).login()
    SecurityNotification(browser).close()
    DashBoardPage(browser).navigate_to_products()
    ProductsPage(browser).delete_product_by_name(config.PRODUCT_NAME)
    assert ProductsPage(browser).is_product_present(config.PRODUCT_NAME) is False, "{0} was removed successfully".format(
        config.PRODUCT_NAME)
