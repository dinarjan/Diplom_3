from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL_FIELD = (By.XPATH, "//input[@type='text']")
    PASSWORD_FIELD = (By.XPATH, "//input[@type='password']")
    ENTER_BUTTON = (By.XPATH, '//button[text()="Войти"]')
    RESET = (By.XPATH, "//a[text()='Восстановить пароль']")