import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.reset_password_page import ResetPasswordPage
from data import Urls


@allure.story('Восстановление пароля')
class TestResetPassword:
    @allure.title("Переход на страницу восстановления пароля по кнопке «Восстановить пароль»")
    def test_go_to_the_password_reset_page(self, driver):
        page = MainPage(driver)
        page.open_main_page()
        page.click_enter_acc_button()
        page = LoginPage(driver)
        page.click_reset()
        assert page.get_page() == Urls.FORGOT_PASSWORD_PAGE, 'Переход на другую страницу'

    @allure.title("Ввод почты и клик по кнопке «Восстановить»")
    def test_enter_mail_and_click_reset(self, driver):
        page = MainPage(driver)
        page.open_main_page()
        page.click_enter_acc_button()
        page = LoginPage(driver)
        page.click_reset()
        page = ResetPasswordPage(driver)
        page.set_email()
        page.click_reset_button()
        assert page.get_page() == Urls.RESET_PASSWORD_PAGE

    @allure.title("Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его")
    def test_active_pass_field(self, driver):
        page = MainPage(driver)
        page.open_main_page()
        page.click_enter_acc_button()
        page = LoginPage(driver)
        page.click_reset()
        page = ResetPasswordPage(driver)
        page.set_email()
        page.click_reset_button()
        page.click_show_pass_button()
        assert page.check_active_field(), 'Поле не активно - не подсвечивается'
