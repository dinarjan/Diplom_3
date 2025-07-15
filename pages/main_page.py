import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from data import Urls


class MainPage(BasePage):
    @allure.step('Переход на главную страницу')
    def open_main_page(self):
        self.driver.get(Urls.MAIN_PAGE)

    @allure.step('Нажать на кнопку «Войти в аккаунт»')
    def click_enter_acc_button(self):
        self.click(MainPageLocators.ENTER_ACC_BUTTON)

    @allure.step('Нажать на «Личный кабинет»')
    def click_my_account(self):
        self.another_click(MainPageLocators.MY_ACCOUNT)

    @allure.step('Нажать на «Конструктор»')
    def click_on_constructor(self):
        self.another_click(MainPageLocators.CONSTRUCTOR)

    @allure.step('Нажать на «Лента заказов»')
    def click_on_order_feed(self):
        self.another_click(MainPageLocators.ORDER_FEED)
