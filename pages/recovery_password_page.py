import allure
from data import TestData
from locators.recovery_locators import TestRecoveryLocators
from selenium.common import NoSuchElementException
from pages.base_page import BasePage

class PasswordRecovery(BasePage):

    @allure.step('Переход на страницу восстановления пароля по кнопке "Восстановить пароль"')
    def enter_page_from_password_recovery(self):
        self.find_element_with_wait(TestRecoveryLocators.ELEMENTS_MAIN_PAGE)
        self.click_element_with_wait(TestRecoveryLocators.BUTTON_ENTER_TO_ACCOUNT)
        self.find_element_with_wait(TestRecoveryLocators.FORM_ENTER_TO_PERSONAL_ACCOUNT)
        self.click_element_with_wait(TestRecoveryLocators.LINK_RECOVERY_PASSWORD)
        self.find_element_with_wait(TestRecoveryLocators.FORM_RECOVERY_PASSWORD)
        try:
            self.find_element_with_wait(TestRecoveryLocators.BUTTON_RESTORE)
            return True
        except NoSuchElementException:
            return False

    @allure.step('Ввод почты и клик по кнопке "Восстановить"')
    def click_restore_button(self):
        self.find_element_with_wait(TestRecoveryLocators.ELEMENTS_MAIN_PAGE)
        self.click_element_with_wait(TestRecoveryLocators.BUTTON_ENTER_TO_ACCOUNT)
        self.find_element_with_wait(TestRecoveryLocators.FORM_ENTER_TO_PERSONAL_ACCOUNT)
        self.click_element_with_wait(TestRecoveryLocators.LINK_RECOVERY_PASSWORD)
        self.find_element_with_wait(TestRecoveryLocators.FORM_RECOVERY_PASSWORD)
        self.enter_text_to_field(TestRecoveryLocators.FIELD_EMAIL, TestData.correct_email)
        self.click_element_with_wait(TestRecoveryLocators.BUTTON_RESTORE)
        self.find_element_with_wait(TestRecoveryLocators.FORM_RECOVERY_PASSWORD_2)
        try:
            self.find_element_with_wait(TestRecoveryLocators.BUTTON_SAVE)
            return True
        except NoSuchElementException:
            return False

    @allure.step('Проверка кнопки показать/скрыть пароль')
    def click_eye_field_password(self):
        self.find_element_with_wait(TestRecoveryLocators.ELEMENTS_MAIN_PAGE)
        self.click_element_with_wait(TestRecoveryLocators.BUTTON_ENTER_TO_ACCOUNT)
        self.find_element_with_wait(TestRecoveryLocators.FORM_ENTER_TO_PERSONAL_ACCOUNT)
        self.click_element_with_wait(TestRecoveryLocators.LINK_RECOVERY_PASSWORD)
        self.find_element_with_wait(TestRecoveryLocators.FORM_RECOVERY_PASSWORD)
        self.enter_text_to_field(TestRecoveryLocators.FIELD_EMAIL, TestData.correct_email)
        self.click_element_with_wait(TestRecoveryLocators.BUTTON_RESTORE)
        self.find_element_with_wait(TestRecoveryLocators.FORM_RECOVERY_PASSWORD_2)
        self.waiting_for_element(TestRecoveryLocators.BUTTON_EYE_PASSWORD)
        try:
            self.find_element_with_wait(TestRecoveryLocators.ACTIVE_PASSWORD_FIELD)
            return True
        except NoSuchElementException:
            return False
