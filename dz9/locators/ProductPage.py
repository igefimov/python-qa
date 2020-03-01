from selenium.webdriver.common.by import By


class ProductPage:
    CART_BUTTON = (By.CSS_SELECTOR, "#button-cart")
    QUANTITY_INPUT = (By.CSS_SELECTOR, "#input-quantity")
    PRODUCT_NAME = (By.CSS_SELECTOR, "#content > div > div.col-sm-4 > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "#content > div > div.col-sm-4 > ul:nth-child(4) > li:nth-child(1) > h2")
    NAVIGATION_TABS = (By.CSS_SELECTOR, "#content > div > div.col-sm-8 > ul.nav.nav-tabs")
    MAIN_IMAGE = (By.CSS_SELECTOR, "#content > div > div.col-sm-8 > ul.thumbnails > li:nth-child(1) > a > img")

