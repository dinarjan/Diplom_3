import allure
from pages.base_page import BasePage
from locators.ingredients_page_locators import IngredientsPageLocators


class IngredientsPage(BasePage):

    @allure.step('Нажать на булку')
    def click_on_bun(self):
        self.click(IngredientsPageLocators.BUN)

    @allure.step('Закрыть окно')
    def click_on_close_button(self):
        self.another_click(IngredientsPageLocators.CLOSE_BUTTON)

    @allure.step('Проверка закрытия всплывающего окна')
    def invis_close_button(self):
        return self.wait_invis(IngredientsPageLocators.CLOSE_BUTTON)

    @allure.step('Добавляем булку в конструктор')
    def add_bun(self):
        source_element = self.find(IngredientsPageLocators.BUN)
        target_element = self.find(IngredientsPageLocators.BURGER_CONSTRUCTOR)
        self.drag_and_drop_element(source_element, target_element)

    @allure.step('Добавляем соус в конструктор')
    def add_sauce(self):
        source_element = self.find(IngredientsPageLocators.SAUCE)
        target_element = self.find(IngredientsPageLocators.BURGER_CONSTRUCTOR)
        self.drag_and_drop_element(source_element, target_element)

    @allure.step('Переход к начинкам')
    def click_on_topping_list(self):
        self.another_click(IngredientsPageLocators.TOPPINGS)
        self.wait_element(IngredientsPageLocators.MEAT)

    @allure.step('Добавляем начинку в конструктор')
    def add_topping(self):
        source_element = self.find(IngredientsPageLocators.MEAT)
        target_element = self.find(IngredientsPageLocators.BURGER_CONSTRUCTOR)
        self.drag_and_drop_element(source_element, target_element)

    @allure.step('Получаем значение каунтера')
    def count_number(self):
        return self.get_text(IngredientsPageLocators.COUNTER)

    def invis_default_number(self):
        return self.wait_invis(IngredientsPageLocators.DEFAULT_NUMBER)

    @allure.step('Получаем номер заказа')
    def get_number_order(self):
        self.visibility_element(IngredientsPageLocators.PREPARED_ORDER)
        self.check_no_text_in_element(IngredientsPageLocators.ORDER_NUMBER, '9999')
        order_id = self.get_text(IngredientsPageLocators.ORDER_NUMBER)
        return order_id

    @allure.step('Создаём заказ')
    def click_on_create_order(self):
        self.another_click(IngredientsPageLocators.CREATE_ORDER)
