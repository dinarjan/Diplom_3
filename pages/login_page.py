import allure
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from data import Urls


class LoginPage(BasePage):
    @allure.step('Нажать на Восстановить пароль')
    def click_reset(self):
        self.click(LoginPageLocators.RESET)

    @allure.step('Вводим данные пользователя')
    def login_user(self, email, password):
        self.add_text(LoginPageLocators.EMAIL_FIELD, email)
        self.add_text(LoginPageLocators.PASSWORD_FIELD, password)
        self.another_click(LoginPageLocators.ENTER_BUTTON)
        self.wait_invis(LoginPageLocators.ENTER_BUTTON)

    @allure.step('Переход на страницу логина')
    def open_login_page(self):
        self.open_link(Urls.LOGIN_PAGE)
