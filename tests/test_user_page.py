import pytest
import allure

from data import TestUrl
from pages.user_page import UserPage
from helpers import WebdriverFactory

class TestUserPage:

    @allure.title('Переход по клику "Личный кабинет"')
    @pytest.mark.parametrize('browser_name', ['chrome', 'firefox'])
    def test_enter_login_to_account(self, browser_name):
        driver = WebdriverFactory().web_driver(browser_name)
        user_page = UserPage(driver)
        driver.get(TestUrl.main_page_url)
        assert user_page.enter_login_to_account() == True
        driver.quit()

    @allure.title('Переход в раздел "История заказов"')
    @pytest.mark.parametrize('browser_name', ['chrome', 'firefox'])
    def test_order_history(self, browser_name):
        driver = WebdriverFactory().web_driver(browser_name)
        user_page = UserPage(driver)
        driver.get(TestUrl.main_page_url)
        assert user_page.order_history() == True
        driver.quit()

    @allure.title('Выход из аккаунта')
    @pytest.mark.parametrize('browser_name', ['chrome', 'firefox'])
    def test_logout_from_account(self, browser_name):
        driver = WebdriverFactory().web_driver(browser_name)
        user_page = UserPage(driver)
        driver.get(TestUrl.main_page_url)
        assert user_page.logout_from_account() == True
        driver.quit()


