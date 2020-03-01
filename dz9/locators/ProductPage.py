from selenium.webdriver.common.by import By


class ProductPage:
    CART_BUTTON = (By.CSS_SELECTOR, "#button-cart")
    QUANTITY_INPUT = (By.CSS_SELECTOR, "#input-quantity")
    FEATURED_LABEL = (By.CSS_SELECTOR, "#content > h3")
    FEATURED_SECTION = (By.CSS_SELECTOR, "#content > div.row")

    # content > div:nth-child(1) > div.col-sm-4 > h1
    # content > div:nth-child(1) > div.col-sm-8 > ul.nav.nav-tabs
    #button-cart

#product-product > ul
PRODUCT_NAME = #content > div > div.col-sm-4 > h1
PRODUCT_PRICE = #content > div > div.col-sm-4 > ul:nth-child(4) > li:nth-child(1) > h2
NAVIGATION_TABS = #content > div > div.col-sm-8 > ul.nav.nav-tabs
#content > div > div.col-sm-8 > ul.thumbnails > li:nth-child(1) > a > img