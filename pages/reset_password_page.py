import allure
from pages.base_page import BasePage
from locators.reset_password_page_locators import ResetPasswordLocators
import helpers


class ResetPasswordPage(BasePage):

    @allure.step('Вводим почту')
    def set_email(self):
        self.add_text(ResetPasswordLocators.EMAIL_FIELD, helpers.create_mail())

    @allure.step('Нажать Восстановить')
    def click_reset_button(self):
        self.click(ResetPasswordLocators.RESET_BUTTON)
        self.wait_element(ResetPasswordLocators.SAVE_PASS_BUTTON)

    @allure.step('Нажать на показать пароль')
    def click_show_pass_button(self):
        self.click(ResetPasswordLocators.SAVE_PASS_BUTTON)

    @allure.step('Проверка активности поля Пароль')
    def check_active_field(self):
        return self.element_is_displayed(ResetPasswordLocators.SHOW_PASS_BUTTON)
