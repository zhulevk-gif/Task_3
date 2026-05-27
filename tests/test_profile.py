import allure

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage


@allure.feature("Личный кабинет")
class TestProfile:

    @allure.title("Открыть личный кабинет")
    @allure.story("Переход из шапки сайта")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_open_personal_account(self, driver, create_user):
        user_data = create_user()

        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        profile_page = ProfilePage(driver)

        main_page.open()
        main_page.open_profile()
        login_page.login(user_data["email"], user_data["password"])
        main_page.open_profile()

        assert profile_page.is_profile_page_opened()

    @allure.title("Открыть историю заказов")
    @allure.story("Переход внутри профиля")
    @allure.severity(allure.severity_level.NORMAL)
    def test_open_order_history(self, driver, create_user):
        user_data = create_user()

        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        profile_page = ProfilePage(driver)

        main_page.open()
        main_page.open_profile()
        login_page.login(user_data["email"], user_data["password"])
        main_page.open_profile()
        profile_page.open_order_history()

        assert profile_page.is_order_history_opened()

    @allure.title("Выйти из аккаунта")
    @allure.story("Авторизация")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_logout_from_account(self, driver, create_user):
        user_data = create_user()

        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        profile_page = ProfilePage(driver)

        main_page.open()
        main_page.open_profile()
        login_page.login(user_data["email"], user_data["password"])
        main_page.open_profile()
        profile_page.click_logout_button()

        assert login_page.is_login_page_opened()