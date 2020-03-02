from selenium.webdriver.common.by import By


class CatalogPage:
    LEFT_SELECTION_PANEL = (By.CSS_SELECTOR, "#column-left")
    SECTION_NAME = (By.CSS_SELECTOR, "#content > h2")
    SECTION_DESCRIPTION = (By.CSS_SELECTOR, "div.col-sm-10 > p")
    SECTION_IMAGE = (By.CSS_SELECTOR, "div.col-sm-2 > img")
