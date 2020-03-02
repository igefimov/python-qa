from selenium.webdriver.common.by import By


class ProductPage:
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "#button-cart")
    QUANTITY_INPUT = (By.CSS_SELECTOR, "#input-quantity")
    PRODUCT_NAME = (By.CSS_SELECTOR, "#content > div > div.col-sm-4 > h1")
    NAVIGATION_TABS = (By.CSS_SELECTOR, "ul.nav-tabs")
    MAIN_IMAGE = (By.CSS_SELECTOR, ".thumbnail > img")
