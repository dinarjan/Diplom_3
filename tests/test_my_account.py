import allure
from pages.main_page import MainPage
from pages.my_account_page import MyAccountPage
from data import Urls


@allure.story('Личный кабинет')
class TestMyAccount:
    @allure.title("Переход в личный кабинет по клику на «Личный кабинет»")
    def test_go_to_the_password_reset_page(self, driver, login):
        page = MainPage(driver)
        page.open_main_page()
        page.click_my_account()
        assert page.get_page() == Urls.ACCOUNT_PAGE, 'Переход на другую страницу'

    @allure.title("Переход в историю заказов по клику на «История заказов»")
    def test_go_the_history_of_orders(self, driver, login):
        page = MainPage(driver)
        page.open_main_page()
        page.click_my_account()
        page = MyAccountPage(driver)
        page.click_on_history()
        assert page.get_page() == Urls.HISTORY_PAGE, 'Переход на другую страницу'

    @allure.title("Выход из аккаунта")
    def test_exit_from_account(self, driver, login):
        page = MainPage(driver)
        page.open_main_page()
        page.click_my_account()
        page = MyAccountPage(driver)
        page.click_exit()
        assert page.get_page() == Urls.LOGIN_PAGE, 'Не удалось выйти из профиля'
