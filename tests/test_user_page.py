import allure

from pages.user_page import UserPage

class TestUserPage:

    @allure.title('Переход по клику "Личный кабинет"')
    def test_enter_login_to_account(self, driver):
        user_page = UserPage(driver)
        assert user_page.enter_login_to_account()

    @allure.title('Переход в раздел "История заказов"')
    def test_order_history(self, driver):
        user_page = UserPage(driver)
        assert user_page.order_history()

    @allure.title('Выход из аккаунта')
    def test_logout_from_account(self, driver):
        user_page = UserPage(driver)
        assert user_page.logout_from_account()


