from selenium.webdriver.common.by import By


class CommonElements:
    OPENCART_URL = "http://192.168.0.122/opencart"
    SEARCH_INPUT = (By.CSS_SELECTOR, "#search > input")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "#search > span > button")
    CART_BUTTON = (By.CSS_SELECTOR, "#cart")