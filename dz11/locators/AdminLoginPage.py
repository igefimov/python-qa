from selenium.webdriver.common.by import By


class AdminLoginPage:
    OPENCART_ADMIN_URL = "http://192.168.0.122/opencart/admin/"
    USERNAME = "admin"
    PASSWORD = "admin"
    USERNAME_INPUT = (By.CSS_SELECTOR, "#input-username")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".btn-primary")
    FORGOTTEN_PASSWORD_LINK = (By.LINK_TEXT, "Forgotten Password")
