from selenium.webdriver.common.by import By


class IngredientsPageLocators:

    BUN = (By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']")
    SAUCE = (By.XPATH, "//img[@alt='Соус Spicy-X']")
    TOPPINGS = (By.XPATH, '//span[text()="Начинки"]')
    MEAT = (By.XPATH, "//img[@alt='Говяжий метеорит (отбивная)']")
    INGREDIENT_DETAILS = (By.XPATH, "//h2[text()='Детали ингредиента']")
    CLOSE_BUTTON = (By.XPATH, '//button[contains(@class,"modal__close")]')
    BURGER_CONSTRUCTOR = (By.XPATH, '//ul[contains(@class,"BurgerConstructor_basket")]')
    COUNTER = (By.XPATH, '//*[@href="/ingredient/61c0c5a71d1f82001bdaaa6d"]//p[contains(@class, "counter__num")]')
    CREATE_ORDER = (By.XPATH, '//button[text()="Оформить заказ"]')
    ORDER_NUMBER = (By.XPATH, '//h2[contains(@class,"title_shadow")]')
    DEFAULT_NUMBER = (By.XPATH, '//h2[text()="9999"]')
    PREPARED_ORDER = (By.XPATH, '//p[text()="Ваш заказ начали готовить"]')
