import allure
from selenium.common import NoSuchElementException
from pages.base_page import BasePage
from data import TestData
from locators.user_locators import TestUserLocators

class UserPage(BasePage):

    @allure.step('Переход по клику "Личный кабинет"')
    def enter_login_to_account(self):
        self.find_element_with_wait(TestUserLocators.ELEMENTS_MAIN_PAGE)
        self.waiting_for_element(TestUserLocators.BUTTON_ENTER_TO_ACCOUNT)
        self.find_element_with_wait(TestUserLocators.FORM_ENTER_TO_PERSONAL_ACCOUNT)
        self.enter_text_to_field(TestUserLocators.FIELD_EMAIL, TestData.correct_email)
        self.enter_text_to_field(TestUserLocators.FIELD_PASSWORD, TestData.correct_password)
        self.waiting_for_element(TestUserLocators.BUTTON_ENTER)
        self.find_element_with_wait(TestUserLocators.ELEMENTS_MAIN_PAGE)
        self.click_element_with_wait(TestUserLocators.LINK_PERSONAL_ACCOUNT)
        try:
            self.find_element_with_wait(TestUserLocators.BUTTON_SAVE)
            return True
        except NoSuchElementException:
            return False

    @allure.step('Переход в раздел "История заказов"')
    def order_history(self):
        self.find_element_with_wait(TestUserLocators.ELEMENTS_MAIN_PAGE)
        self.waiting_for_element(TestUserLocators.BUTTON_ENTER_TO_ACCOUNT)
        self.find_element_with_wait(TestUserLocators.FORM_ENTER_TO_PERSONAL_ACCOUNT)
        self.enter_text_to_field(TestUserLocators.FIELD_EMAIL, TestData.correct_email)
        self.enter_text_to_field(TestUserLocators.FIELD_PASSWORD, TestData.correct_password)
        self.click_element(TestUserLocators.BUTTON_ENTER)
        self.find_element_with_wait(TestUserLocators.ELEMENTS_MAIN_PAGE)
        self.click_element_with_wait(TestUserLocators.LINK_PERSONAL_ACCOUNT)
        self.waiting_for_element(TestUserLocators.BUTTON_HISTORY_ORDERS)
        try:
            self.find_element_with_wait(TestUserLocators.LIST_USER_ORDERS)
            return True
        except NoSuchElementException:
            return False

    @allure.step('Выход из аккаунта')
    def logout_from_account(self):
        self.find_element_with_wait(TestUserLocators.ELEMENTS_MAIN_PAGE)
        self.waiting_for_element(TestUserLocators.BUTTON_ENTER_TO_ACCOUNT)
        self.find_element_with_wait(TestUserLocators.FORM_ENTER_TO_PERSONAL_ACCOUNT)
        self.enter_text_to_field(TestUserLocators.FIELD_EMAIL, TestData.correct_email)
        self.enter_text_to_field(TestUserLocators.FIELD_PASSWORD, TestData.correct_password)
        self.click_element(TestUserLocators.BUTTON_ENTER)
        self.find_element_with_wait(TestUserLocators.ELEMENTS_MAIN_PAGE)
        self.click_element_with_wait(TestUserLocators.LINK_PERSONAL_ACCOUNT)
        self.waiting_for_element(TestUserLocators.BUTTON_LOGOUT)
        try:
            self.find_element_with_wait(TestUserLocators.BUTTON_ENTER)
            return True
        except NoSuchElementException:
            return False








