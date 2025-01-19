import pytest
import allure

from helpers import WebdriverFactory
from data import TestUrl
from pages.recovery_password_page import PasswordRecovery

class TestPasswordRecovery:

    @allure.title('Переход на страницу восстановления пароля по кнопке "Восстановить пароль"')
    @pytest.mark.parametrize('browser_name', ['chrome', 'firefox'])
    def test_enter_page_from_password_recovery(self, browser_name):
        driver = WebdriverFactory().web_driver(browser_name)
        password_recovery_page = PasswordRecovery(driver)
        driver.get(TestUrl.main_page_url)
        assert password_recovery_page.enter_page_from_password_recovery() == True
        driver.quit()

    @allure.title('Ввод почты и клик по кнопке "Восстановить"')
    @pytest.mark.parametrize('browser_name', ['chrome', 'firefox'])
    def test_click_restore_button(self, browser_name):
        driver = WebdriverFactory().web_driver(browser_name)
        password_recovery_page = PasswordRecovery(driver)
        driver.get(TestUrl.main_page_url)
        assert password_recovery_page.click_restore_button() == True
        driver.quit()

    @allure.title('Проверка кнопки показать/скрыть пароль')
    @pytest.mark.parametrize('browser_name', ['chrome', 'firefox'])
    def test_click_eye_field_password(self, browser_name):
        driver = WebdriverFactory().web_driver(browser_name)
        password_recovery_page = PasswordRecovery(driver)
        driver.get(TestUrl.main_page_url)
        assert password_recovery_page.click_eye_field_password() == True
        driver.quit()


