from selenium.webdriver.common.by import By


class CommonElements:
    OPENCART_URL = "https://demo.opencart.com/"
    SEARCH_INPUT = (By.CSS_SELECTOR, "#search > input")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "#search > span > button")
    CART_BUTTON = (By.CSS_SELECTOR, "#cart")