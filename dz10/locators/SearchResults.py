from selenium.webdriver.common.by import By


class SearchResults:
    SEARCH_TOPIC = (By.CSS_SELECTOR, "#content > h1")
    SEARCH_CRITERIA_INPUT = (By.CSS_SELECTOR, "#input-search")
    SEARCH_CRITERIA_CATEGORY = (By.NAME, "category_id")
    SEARCH_IN_PRODUCT_DESCRIPTION = (By.CSS_SELECTOR, "#description")
    SEARCH_IN_SUBCATEGORIES = (By.NAME, "sub_category")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "#button-search")
