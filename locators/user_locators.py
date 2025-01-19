from selenium.webdriver.common.by import By

class TestUserLocators:
    ELEMENTS_MAIN_PAGE = By.CLASS_NAME, "BurgerIngredients_ingredients__1N8v2" #Для проверки загрузки главной страницы
    BUTTON_ENTER_TO_ACCOUNT = By.XPATH, ".//section[2]//button[text()='Войти в аккаунт']" #Кнопка "Войти в аккаунт"
    LINK_PERSONAL_ACCOUNT = By.LINK_TEXT, "Личный Кабинет"  # Кнопка-ссылка "Личный кабинет"
    #LINK_PERSONAL_ACCOUNT = By.XPATH, ".//a[@class='AppHeader_header__link__3D_hX AppHeader_header__link_active__1IkJo']"
    #BUTTON_SAVE = By.XPATH, ".//img[@class='Modal_modal__loading__3534A']"  # Кнопка "Сохранить"
    BUTTON_SAVE = By.XPATH, ".//button[text()='Сохранить']"
    FORM_ENTER_TO_PERSONAL_ACCOUNT = By.XPATH, ".//form[@class='Auth_form__3qKeq mb-20']" #Форма для входа в личный кабинет
    FIELD_EMAIL = By.XPATH, ".//label[text()='Email']/following-sibling::input" #Поле ввода эл.почты
    FIELD_PASSWORD = By.XPATH, ".//label[text()='Пароль']/following-sibling::input" #Поле ввода пароля
    BUTTON_ENTER = By.XPATH, ".//button[text()='Войти']" #Кнопка "Войти
    BUTTON_PLACE_AN_ORDER = By.XPATH, ".//section[2]//button[text()='Оформить заказ']" #Кнопка "Оформить заказ"
    BUTTON_PERSONAL_ACCOUNT = By.LINK_TEXT, "Личный Кабинет"  # Кнопка-ссылка "Личный кабинет"
    BUTTON_HISTORY_ORDERS = By.XPATH, ".//ul[@class='Account_list__3KQQf mb-20']/li[2]/a[text()='История заказов']" #Кнопка "История заказов"
    LIST_BUTTONS_PERSONAL_ACCOUNT = By.XPATH, ".//ul[@class='Account_list__3KQQf mb-20']" #Список кнопок в личном кабинете
   # ELEMENTS_HISTORY_ORDERS = By.XPATH, ".//div[@class='OrderHistory_orderHistory__qy1VB']" #Элементы истории заказов
    LIST_USER_ORDERS = By.XPATH, ".//ul[@class='OrderHistory_profileList__374GU OrderHistory_list__KcLDB']/li[1]/a" #Список заказов
    BUTTON_LOGOUT = By.XPATH, ".//ul[@class='Account_list__3KQQf mb-20']/li[3]/button[text()='Выход']" #Кнопка "Выход"
  #  INGREDIENT = By.XPATH, ".//img[@alt={}]" #Ингредиенты
   # FORM_FOR_ORDER = By.XPATH, ".//selection[@class='BurgerConstructor_basket__29Cd7 mt-25 ']"
   # WINDOW_ORDER = By.XPATH, ".//div[@class='Modal_modal__container__Wo2l_']"

