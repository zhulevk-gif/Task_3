import allure

from pages.forgot_password_page import ForgotPasswordPage
from pages.login_page import LoginPage


@allure.feature("Восстановление пароля")
class TestForgotPassword:

    @allure.title("Открыть страницу восстановления пароля")
    @allure.story("Переход из формы входа")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_open_forgot_password_page(self, driver):
        login_page = LoginPage(driver)
        forgot_password_page = ForgotPasswordPage(driver)

        login_page.open()
        login_page.open_forgot_password_page()

        assert forgot_password_page.is_forgot_password_page_opened()

    @allure.title("Заполнить email и нажать восстановление")
    @allure.story("Отправка формы восстановления")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_fill_email_and_click_restore(self, driver, create_user):
        user_data = create_user()

        login_page = LoginPage(driver)
        forgot_password_page = ForgotPasswordPage(driver)

        login_page.open()
        login_page.open_forgot_password_page()
        forgot_password_page.enter_email(user_data["email"])
        forgot_password_page.click_restore_button()

        assert forgot_password_page.is_reset_password_page_opened()

    @allure.title("Кнопка глаза делает поле активным")
    @allure.story("Показ пароля")
    @allure.severity(allure.severity_level.NORMAL)
    def test_password_eye_button_makes_field_active(self, driver, create_user):
        user_data = create_user()

        login_page = LoginPage(driver)
        forgot_password_page = ForgotPasswordPage(driver)

        login_page.open()
        login_page.open_forgot_password_page()
        forgot_password_page.enter_email(user_data["email"])
        forgot_password_page.click_restore_button()

        assert forgot_password_page.is_reset_password_page_opened()

        forgot_password_page.click_password_eye_button()

        assert forgot_password_page.is_active_password_field()