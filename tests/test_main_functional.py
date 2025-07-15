import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.ingredients_page import IngredientsPage
from data import Urls


@allure.story('Проверка основного функционала')
class TestMainFunctional:
    @allure.title("Переход по клику на «Конструктор»")
    def test_click_on_constructor_button(self, driver):
        page = LoginPage(driver)
        page.open_login_page()
        page = MainPage(driver)
        page.click_on_constructor()
        assert page.get_page() == Urls.MAIN_PAGE, 'Нет перехода по клику'

    @allure.title("Переход по клику на «Лента заказов»")
    def test_click_on_order_feed(self, driver):
        page = LoginPage(driver)
        page.open_login_page()
        page = MainPage(driver)
        page.click_on_order_feed()
        assert page.get_page() == Urls.FEED_PAGE, 'Нет перехода по клику'

    @allure.title("По клику на ингредиент появится всплывающее окно с деталями")
    def test_popup_window_with_ingredient_details(self, driver):
        page = MainPage(driver)
        page.open_main_page()
        page.click_on_constructor()
        page = IngredientsPage(driver)
        page.click_on_bun()
        curr_url = page.get_page()
        ingr_id = curr_url.split("/")[-1]
        assert ingr_id in page.get_page(), 'Всплывающее окно не появилось'

    @allure.title("Всплывающее окно закрывается кликом по крестику")
    def test_close_popup_windows_with_ingredient_details(self, driver):
        page = MainPage(driver)
        page.open_main_page()
        page.click_on_constructor()
        page = IngredientsPage(driver)
        page.click_on_bun()
        page.click_on_close_button()
        assert page.invis_close_button()

    @allure.title("При добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента")
    def test_counter(self, driver):
        page = MainPage(driver)
        page.open_main_page()
        page.click_on_constructor()
        page = IngredientsPage(driver)
        page.add_bun()
        assert int(page.count_number()) == 2

    @allure.title("Залогиненный пользователь может оформить заказ")
    def test_create_order_after_login_user(self, driver, login):
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
        order_id = page.get_number_order()
        assert order_id, 'Заказ не создался'
