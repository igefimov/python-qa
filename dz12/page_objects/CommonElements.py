from selenium.webdriver.common.by import By


class CommonElements:
    OPENCART_LOGO = (By.CSS_SELECTOR, "#header-logo")
    LEFT_MENU_CATALOG = (By.CSS_SELECTOR, "#menu-catalog")
    LEFT_MENU_CATALOG_CATEGORY = (By.CSS_SELECTOR, "#collapse1 > li")
    LEFT_MENU_CATALOG_LAST_CATEGORY = (By.CSS_SELECTOR, "#collapse1 > :nth-child(10)")
    SECURITY_NOTIFICATION = (By.CSS_SELECTOR, ".close")
