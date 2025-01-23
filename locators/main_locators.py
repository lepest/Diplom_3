from selenium.webdriver.common.by import By

class TestMainPageLocators:
    ELEMENTS_MAIN_PAGE = By.CLASS_NAME, "BurgerIngredients_ingredients__1N8v2"  # Для проверки загрузки главной страницы
    ORDER_FEED = By.XPATH, ".//ul[@class='AppHeader_header__list__3oKJj']/li[@class='undefined ml-2']/a[@href='/feed']" #Кнопка "Лента заказов"
    BUTTON_ENTER_TO_ACCOUNT = By.XPATH, ".//div[@class='BurgerConstructor_basket__container__2fUl3 mt-10']/button[text()='Войти в аккаунт']"  # Кнопка "Войти в аккаунт"
    FORM_ENTER_TO_PERSONAL_ACCOUNT = By.XPATH, ".//form[@class='Auth_form__3qKeq mb-20']"  # Форма для входа в личный кабинет
    BUTTON_CONSTRUCTOR = By.XPATH, ".//ul[@class='AppHeader_header__list__3oKJj']/li/a[@class='AppHeader_header__link__3D_hX' and @href='/']"
    HEADER_ORDER_FEED = By.XPATH, ".//h1[text()='Лента заказов']" #Заголовок "Лента заказов"
    LIST_ORDERS = By.XPATH, ".//ul[@class='OrderFeed_list__OLh59']" #Список заказов
    BUTTON_CLOSE_POPUP_WINDOW = By.XPATH, "//section[@class='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']/div/button" #Кнопка-крестик, закрывающий всплывающее окно
    MODAL_WINDOW = By.XPATH, ".//section/div[@class='Modal_modal_overlay__x2ZCr']"
    POPUP_WINDOW = By.XPATH, ".//div[@class='Modal_modal__container__Wo2l_']" #Всплывающее окно
    WINDOW_SUCCESSFUL_ORDER = By.XPATH, ".//div[@class='Modal_modal__textContainer__9TwLS']/p[@class='undefined text text_type_main-small mb-2']" #Текст об успешном оформлении заказа, в окне
    HEADER_CONSTRUCTOR = By.XPATH, ".//h1[@class='text text_type_main-large mb-5 mt-10']" #Заголовок страницы конструктора
    INGREDIENT_CONSTRUCTOR = By.XPATH, ".//ul[@class='BurgerIngredients_ingredients__list__2A-mT'][1]/a[1]" #Ингредиент на странице конструктора
    NAME_INGREDIENT_CONSTRUCTOR_ = By.XPATH, ".//div[@class='Modal_modal__contentBox__sCy8X pt-10 pb-15']/p" #Имя ингредиента
    COUNTER_INGREDIENT_CONSTRUCTOR = By.XPATH, ".//a[1]/div[@class='counter_counter__ZNLkj counter_default__28sqi']/p" #Счётчик ингредиента
    CONSTRUCTOR_LIST = By.XPATH, ".//div[@class='BurgerIngredients_ingredients__menuContainer__Xu3Mo']" #Список ингредиентов
    CONSTRUCTOR_BASKET = By.XPATH, ".//ul[@class='BurgerConstructor_basket__list__l9dp_']" #Корзина для заказа
    FIELD_EMAIL = By.XPATH, ".//label[text()='Email']/following-sibling::input"  # Поле ввода эл.почты
    FIELD_PASSWORD = By.XPATH, ".//label[text()='Пароль']/following-sibling::input"  # Поле ввода пароля
    BUTTON_ENTER = By.XPATH, ".//button[text()='Войти']"  # Кнопка "Войти
    BUTTON_PLACE_AN_ORDER = By.XPATH, ".//section[2]/div[@class='BurgerConstructor_basket__container__2fUl3 mt-10']/button"  # Кнопка "Оформить заказ"
    NUMBER_ORDER_IN_POPUP_WINDOW = By.XPATH, ".//div[@class='Modal_modal__contentBox__sCy8X pt-30 pb-30']/h2"  # Номер заказа во вслывающем окне