from selenium.webdriver.common.by import By

class TestRecoveryLocators:
    ELEMENTS_MAIN_PAGE = By.CLASS_NAME, "BurgerIngredients_ingredients__1N8v2" #Для проверки загрузки главной страницы
    BUTTON_ENTER_TO_ACCOUNT = By.XPATH, ".//section[2]//button[text()='Войти в аккаунт']" #Кнопка "Войти в аккаунт"
    FORM_ENTER_TO_PERSONAL_ACCOUNT = By.XPATH, ".//form[@class='Auth_form__3qKeq mb-20']" #Форма для входа в личный кабинет
    LINK_RECOVERY_PASSWORD = By.LINK_TEXT, "Восстановить пароль" #Кнопка-ссылка "Восстановить пароль"
    FORM_RECOVERY_PASSWORD = By.XPATH, ".//div[@class='Auth_login__3hAey']" #Форма восстановления пароля
    BUTTON_RESTORE = By.XPATH, ".//button[text()='Восстановить']"  #Кнопка "Восстановить"
    FIELD_EMAIL = By.XPATH, ".//label[text()='Email']/following-sibling::input"  #Поле ввода эл.почты
    BUTTON_SAVE = By.XPATH, ".//img[@class='Modal_modal__loading__3534A']"  # Кнопка "Сохранить"
    FORM_RECOVERY_PASSWORD_2 = By.XPATH, ".//form[@class='Auth_form__3qKeq mb-20']" #Форма восстановления пароля - 2
    BUTTON_EYE_PASSWORD = By.XPATH, ".//fieldset/div/div/div[@class='input__icon input__icon-action']"
    ACTIVE_PASSWORD_FIELD = By.XPATH, ".//div[@class='input pr-6 pl-6 input_type_text input_size_default input_status_active']/input[@type='text']"