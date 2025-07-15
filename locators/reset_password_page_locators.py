from selenium.webdriver.common.by import By


class ResetPasswordLocators:
    EMAIL_FIELD = (By.XPATH, "//input[@type='text']")
    RESET_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    PASSWORD_FIELD = (By.XPATH, "//input[@type='password']")
    SAVE_PASS_BUTTON = (By.XPATH, "//button[text()='Сохранить']")
    SHOW_PASS_BUTTON = (By.XPATH, '//div[contains(@class,"icon-action")]')
