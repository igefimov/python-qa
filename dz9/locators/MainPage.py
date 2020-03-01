from selenium.webdriver.common.by import By


class MainPage:
    SLIDER_SHOW = (By.CSS_SELECTOR, "#slideshow0")
    BOTTOM_CAROUSEL = (By.CSS_SELECTOR, "#carousel0")
    FEATURED_LABEL = (By.CSS_SELECTOR, "#content > h3")
    FEATURED_SECTION = (By.CSS_SELECTOR, "#content > div.row")
    # content > div.row > div:nth-child(1)
    # content > div.row > div:nth-child(2)
    # content > div.row
