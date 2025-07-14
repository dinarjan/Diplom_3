import allure
from pages.main_page import MainPage
from pages.ingredients_page import IngredientsPage
from pages.order_feed_page import OrderFeedPage


@allure.story("Раздел «Лента заказов»")
class TestOrderFeed:

    @allure.title("Если кликнуть на заказ, откроется всплывающее окно с деталями")
    def test_order_popup(self, driver):
        page = OrderFeedPage(driver)
        page.open_order_feed_page()
        page.click_on_last_order()
        assert page.wait_structure(), 'Окно с деталями заказа не появляется'

    @allure.title("Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»")
    def test_displaying_orders(self, driver, login):
        page = MainPage(driver)
        page.open_main_page()
        page.click_on_constructor()
        page = IngredientsPage(driver)
        page.add_bun()
        page.add_sauce()
        page.click_on_topping_list()
        page.add_topping()
        page.click_on_create_order()
        page.invis_default_number()
        order_id = f"#0{page.get_number_order()}"
        page.click_on_close_button()
        page.invis_close_button()
        page = MainPage(driver)
        page.click_on_order_feed()
        page = OrderFeedPage(driver)
        page.click_on_last_order()
        assert page.element_displayed(order_id=order_id)

    @allure.title("При создании нового заказа счётчик Выполнено за всё время увеличивается")
    def test_counter_orders_for_all_time(self, driver, login):
        page = MainPage(driver)
        page.click_on_order_feed()
        page = OrderFeedPage(driver)
        orders_counter = page.get_all_orders()
        page = MainPage(driver)
        page.open_main_page()
        page.click_on_constructor()
        page = IngredientsPage(driver)
        page.add_bun()
        page.add_sauce()
        page.click_on_topping_list()
        page.add_topping()
        page.click_on_create_order()
        page.invis_default_number()
        page.click_on_close_button()
        page.invis_close_button()
        page = MainPage(driver)
        page.click_on_order_feed()
        page = OrderFeedPage(driver)
        new_orders_counter = page.get_all_orders()
        assert new_orders_counter > orders_counter

    @allure.title("При создании нового заказа счётчик Выполнено за сегодня увеличивается")
    def test_counter_orders_for_today(self, driver, login):
        page = MainPage(driver)
        page.click_on_order_feed()
        page = OrderFeedPage(driver)
        orders_counter = page.get_today_orders()
        page = MainPage(driver)
        page.open_main_page()
        page.click_on_constructor()
        page = IngredientsPage(driver)
        page.add_bun()
        page.add_sauce()
        page.click_on_topping_list()
        page.add_topping()
        page.click_on_create_order()
        page.invis_default_number()
        page.click_on_close_button()
        page.invis_close_button()
        page = MainPage(driver)
        page.click_on_order_feed()
        page = OrderFeedPage(driver)
        new_orders_counter = page.get_today_orders()
        assert new_orders_counter > orders_counter

    @allure.title("После оформления заказа его номер появляется в разделе В работе")
    def test_order_in_work(self, driver, login):
        page = MainPage(driver)
        page.open_main_page()
        page.click_on_constructor()
        page = IngredientsPage(driver)
        page.add_bun()
        page.add_sauce()
        page.click_on_topping_list()
        page.add_topping()
        page.click_on_create_order()
        page.invis_default_number()
        order_number = f"0{page.get_number_order()}"
        page.click_on_close_button()
        page.invis_close_button()
        page = MainPage(driver)
        page.click_on_order_feed()
        page = OrderFeedPage(driver)
        order_in_work = page.get_text_work()
        assert order_number in order_in_work
