import allure
from pages.base_page import BasePage
from locators.my_account_page_locators import MyAccountLocators


class MyAccountPage(BasePage):

    @allure.step('Нажать на историю заказов')
    def click_on_history(self):
        self.another_click(MyAccountLocators.ORDER_HISTORY)

    @allure.step('Выход из профиля')
    def click_exit(self):
        self.another_click(MyAccountLocators.EXIT_BUTTON)
        self.wait_invis(MyAccountLocators.EXIT_BUTTON)
