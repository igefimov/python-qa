from selenium.webdriver.common.by import By

class AdminLoginPage:
    USERNAME_INPUT = (By.CSS_SELECTOR, "#input-username")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#input-password")
    LOGIN_BUTTON = (By.CLASS_NAME, "btn-primary")
    FORGOTTEN_PASSWORD_LINK = (By.LINK_TEXT, "Forgotten Password")
    OPENCART_LOGO = (By.CSS_SELECTOR, "#header-logo")
