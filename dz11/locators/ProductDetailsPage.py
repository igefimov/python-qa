from selenium.webdriver.common.by import By


class ProductDetailsPage:
    PRODUCT_NAME_INPUT = (By.CSS_SELECTOR, "#input-name1")
    META_TITLE_INPUT = (By.CSS_SELECTOR, "#input-meta-title1")
    DATA_TAB = (By.CSS_SELECTOR, "#form-product li:nth-child(2)")
    MODEL_INPUT = (By.CSS_SELECTOR, "#input-model")
    SAVE_BUTTON = (By.CSS_SELECTOR, ".btn-primary")
    ALERT_SUCCESS = (By.CSS_SELECTOR, ".alert-success")
