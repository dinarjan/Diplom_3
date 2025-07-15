from selenium.webdriver.common.by import By


class OrderFeedLocators:
    LAST_ORDER = (By.XPATH, "//a[contains(@class, 'OrderHistory_link')]")
    STRUCTURE = (By.XPATH, '//p[text()="Cостав"]')
    ORDERS_ALL_TIME = (By.XPATH, '//p[text()="Выполнено за все время:"]/following-sibling::p[contains(@class,"OrderFeed_number")]')
    ORDERS_TODAY = (By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p[contains(@class,"OrderFeed_number")]')
    IN_WORK = (By.XPATH, '//*[contains(@class,"orderListReady")]//li[contains(@class,"digits-default")]')
