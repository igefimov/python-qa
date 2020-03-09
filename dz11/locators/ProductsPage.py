from selenium.webdriver.common.by import By


class ProductsPage:
    PRODUCT_TABLE = (By.CSS_SELECTOR, ".table-responsive")
    ADD_NEW_PRODUCT_BUTTON = (By.CSS_SELECTOR, ".btn-primary")
    PRODUCT_NAME_INPUT = (By.CSS_SELECTOR, "#input-name")
    FILTER_BUTTON = (By.CSS_SELECTOR, "#button-filter")
    CHECKBOX_ALL = (By.CSS_SELECTOR, "#form-product input[type=checkbox]")
    DELETE_BUTTON = (By.CSS_SELECTOR, ".btn-danger")
    EDIT_PRODUCT_BUTTON = (By.CSS_SELECTOR, "#form-product .btn-primary")

