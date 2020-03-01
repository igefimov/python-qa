from selenium.webdriver.common.by import By


class CommonElements:
    SEARCH_INPUT = (By.CSS_SELECTOR, "#search > input")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "#search > span > button")
