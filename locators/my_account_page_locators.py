from selenium.webdriver.common.by import By


class MyAccountLocators:
    ORDER_HISTORY = (By.XPATH, "//a[text()='История заказов']")
    EXIT_BUTTON = (By.XPATH, '//*[contains(@class, "Account_button")]')

