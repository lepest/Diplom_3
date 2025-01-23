import allure

from pages.recovery_password_page import PasswordRecovery

class TestPasswordRecovery:

    @allure.title('Переход на страницу восстановления пароля по кнопке "Восстановить пароль"')
    def test_enter_page_from_password_recovery(self, driver):
        password_recovery_page = PasswordRecovery(driver)
        assert password_recovery_page.enter_page_from_password_recovery()

    @allure.title('Ввод почты и клик по кнопке "Восстановить"')
    def test_click_restore_button(self, driver):
        password_recovery_page = PasswordRecovery(driver)
        assert password_recovery_page.click_restore_button()

    @allure.title('Проверка кнопки показать/скрыть пароль')
    def test_click_eye_field_password(self, driver):
        password_recovery_page = PasswordRecovery(driver)
        assert password_recovery_page.click_eye_field_password()


