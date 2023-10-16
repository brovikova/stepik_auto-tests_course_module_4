from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class BasketPageLocators():
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a.btn.btn-default")
    BASKET_FORM = (By.ID, "#basket_formset")
    # BASKET_EMPTY = (By.CSS_SELECTOR, "#content_inner:not(form)")
    BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")

    PRICE = (
        By.XPATH, "//div[@class='col-sm-6 product_main']//p[@class='price_color']")
    PRICE_MESSAGE = (
        By.CSS_SELECTOR, "#messages .alert-info .alertinner strong")

    BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
    SUCCESS_MESSAGE = (
        By.CSS_SELECTOR, "#messages .alert-success:first-child .alertinner strong")
