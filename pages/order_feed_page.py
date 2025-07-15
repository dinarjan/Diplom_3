import allure
from pages.base_page import BasePage
from data import Urls
from locators.order_feed_page_locators import OrderFeedLocators
from helpers import get_order_id


class OrderFeedPage(BasePage):

    @allure.step('Переход на страницу заказов')
    def open_order_feed_page(self):
        self.open_link(Urls.FEED_PAGE)

    @allure.step('Нажать на последний созданный заказ')
    def click_on_last_order(self):
        self.another_click(OrderFeedLocators.LAST_ORDER)

    @allure.step('Проверка появления всплывающего окна с деталями заказа')
    def wait_structure(self):
        return self.element_is_displayed(OrderFeedLocators.STRUCTURE)

    @allure.step('Проверка отображения заказа пользователя')
    def element_displayed(self, order_id):
        return self.element_is_displayed(get_order_id(order_id))

    @allure.step('Получаем число выполненных заказов за всё время')
    def get_all_orders(self):
        return self.get_text(OrderFeedLocators.ORDERS_ALL_TIME)

    @allure.step('Получаем число выполненных заказов за сегодня')
    def get_today_orders(self):
        return self.get_text(OrderFeedLocators.ORDERS_TODAY)

    @allure.step('Получаем номер заказа, который в работе')
    def get_text_work(self):
        return self.get_text(OrderFeedLocators.IN_WORK)
