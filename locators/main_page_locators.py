from selenium.webdriver.common.by import By


class MainPageLocators:
    CONSTRUCTOR = (By.XPATH, "//p[text()='Конструктор']")
    ORDER_FEED = (By.XPATH, "//p[text()='Лента Заказов']")
    MY_ACCOUNT = (By.XPATH, "//p[text()='Личный Кабинет']")
    CLOSE_BUTTON = (By.CSS_SELECTOR, "button.modal__close")
    ENTER_ACC_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    INGREDIENT = (By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']")
