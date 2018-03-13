# -*- coding: utf-8 -*-
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains as ac
from time import sleep
import pdb


TIME_OUT = 10


class BasePage(object):

    xpath_region = '//div[3]/div[3]/div/div/div[2]/div[1]/span'
    xpath_login = '//div[1]/div[1]/noindex/div[2]/div/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/div/div/a'
    xpath_city = '//div[1]/div[1]/div[1]/noindex/div[2]/div/div[2]/div/div[2]/div[1]/span/span[2]'
    xpath_new_city = '//div[4]/div/div/div[1]/div[1]/form/div/div/div/div[1]/span/input'
    xpath_change_city = '//div[3]/div[3]/div/div/div[2]/div[2]/span'
    xpath_go_button = '//div[4]/div/div/div[1]/div[1]/form/div/button'

    login_button = (By.XPATH, xpath_login)
    region = (By.XPATH, xpath_region)
    city = (By.XPATH, xpath_city)
    new_city = (By.XPATH, xpath_new_city)
    go_button = (By.XPATH, xpath_go_button)
    change_city = (By.XPATH, xpath_change_city)

    def __init__(self, browser):
        self.driver = browser
        self.wait = WebDriverWait(browser, TIME_OUT)

    def find_element(self, locator):
        return self.wait.until(ec.presence_of_element_located(locator))

    def find_elements(self, locator):
        return self.wait.until(ec.presence_of_all_elements_located(locator))

    # def set_city(self, city):
    #     self.find_element(self.city).click()
    #     self.find_element(self.new_city).send_keys(city)
    #     self.find_element(self.go_button).click()

    def set_region(self, region):

        try:
            self.find_element(self.change_city).click()
        except TimeoutException:
            self.find_element(self.city).click()

        self.find_element(self.new_city).send_keys(region)
        self.find_element(self.go_button).send_keys(Keys.ENTER)
        pdb.set_trace()
        self.find_element(self.go_button).click()
        return BasePage(self.driver)

    def login(self):
        self.find_element(self.login_button).click()
        windows = self.driver.window_handles
        self.driver.switch_to_window(windows[1])
        return LoginPage(self.driver)


class LoginPage(BasePage):

    username = (By.NAME, 'login')
    password = (By.NAME, 'passwd')
    login_button = (By.CSS_SELECTOR, 'span.passport-Button-Text')

    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)

    def enter_username(self, username):
        self.find_element(self.username).send_keys(username)
        return LoginPage(self.driver)

    def enter_password(self, password):
        self.find_element(self.password).send_keys(password)
        return LoginPage(self.driver)

    def sign_in(self):
        self.find_element(self.login_button).click()
        windows = self.driver.window_handles
        self.driver.switch_to_window(windows[0])
        return HomePage(self.driver)


class HomePage(BasePage):

    avatar = (By.CSS_SELECTOR, 'span.user__icon')
    search_field = (By.ID, 'header-search')
    search_button = (By.XPATH, '//div[1]/div[1]/noindex/div[2]/div/div[2]/div/div[1]/form/span[2]/button')

    def __init__(self, driver):
        super(HomePage, self).__init__(driver)

    def is_loaded(self):
        try:
            self.find_element(self.avatar)
            return True
        except NoSuchElementException:
            return False

    def search(self, item):
        self.find_element(self.search_field).send_keys(item)
        self.find_element(self.search_button).click()
        return ResultsPage(self.driver)


class QuickSearchPage(BasePage):

    expand_results_link = (By.XPATH, '//div[1]/div[3]/div/div/div/div[1]/a')

    def __init__(self, driver):
        super(QuickSearchPage, self).__init__(driver)

    def expand_results(self):
        self.find_element(self.expand_results_link).click()
        return ResultsPage(self.driver)


class ResultsPage(BasePage):

    xpath_expand_search = '//div[1]/div[3]/div/div/div/div[1]/a'
    xpath_order_on_market = '//div[1]/div[4]/div[2]/div[2]/div[2]/div/div[3]/div/div[1]/div/span/label/span'
    xpath_order_by_price = '//div[1]/div[4]/div[1]/div[2]/div[1]/div[1]/div[3]/a'
    xpath_first_result = '//div[1]/div[4]/div[2]/div[1]/div[2]/div/div[1]/div/div[4]/div[1]/div/a'

    expand_results_link = (By.XPATH, xpath_expand_search)
    order_on_market_tick_box = (By.XPATH, xpath_order_on_market)
    sort_by_price_filter = (By.XPATH, xpath_order_by_price)
    first_result = (By.XPATH, xpath_first_result)

    def __init__(self, driver):
        super(ResultsPage, self).__init__(driver)

    def expand_results(self):
        self.find_element(self.expand_results_link).click()
        return ResultsPage(self.driver)

    def order_on_market(self):
        self.find_element(self.order_on_market_tick_box).click()
        return ResultsPage(self.driver)

    def sort_by_price(self):
        self.find_element(self.sort_by_price_filter).click()
        return ResultsPage(self.driver)

    def get_first_result(self):
        return self.find_element(self.first_result)

    def get_product_details(self):
        pdb.set_trace()
        self.find_element(self.first_result).click()
        return ProductPage(self.driver)


class ProductPage(BasePage):

    xpath_add_to_cart = '//div[1]/div[4]/div[4]/div[3]/div/div/div/div[5]/div/a'
    xpath_go_to_card = '//div[3]/div/div/div[1]/div[1]/div/div/div/div[1]/div[2]/div[1]/a/span[2]'
    to_cart = (By.XPATH, xpath_add_to_cart)
    go_to_cart_button = (By.XPATH, xpath_go_to_card)

    def __init__(self, driver):
        super(ProductPage, self).__init__(driver)

    def add_to_cart(self):
        self.find_element(self.to_cart).click()
        return ProductPage(self.driver)

    def go_to_cart(self):
        pdb.set_trace()
        self.find_element(self.go_to_cart_button).click()
        return CartPage(self.driver)


class CartPage(BasePage):

    xpath_item = '//div[1]/div[2]/div[1]/div[3]/div//div[2]/div//div[2]/div//div'
    xpath_place_order = '//*[@id="scroll-to-cart-group-178623"]/div/div[2]/div[2]/div/div[2]/div/div[2]/button'

    item_to_purchase = (By.PARTIAL_LINK_TEXT, 'iPhone 7 128G')
    place_order_button = (By.XPATH, xpath_place_order)

    def __init__(self, driver):
        super(CartPage, self).__init__(driver)

    def product_in_cart(self):
        pdb.set_trace()
        return self.find_element(self.item_to_purchase).text

    def place_order(self):
        self.find_element(self.place_order_button).click()
        return OrderPage(self.driver)


class OrderPage(BasePage):

    item_to_order = (By.CSS_SELECTOR, 'div.n-checkout-offer__item-name')
    name = (By.NAME, 'user-name')
    email = (By.NAME, 'user-email')
    delete_item = (By.CSS_SELECTOR, 'div.image.image_name_trash')
    select_product_button = (By.CSS_SELECTOR, 'div.n-w-checkout__text')
    avatar = (By.CSS_SELECTOR, 'span.user__icon')
    logout_link = (By.LINK_TEXT, 'Выйти')

    def __init__(self, driver):
        super(OrderPage, self).__init__(driver)

    def get_order_details(self):
        return self.find_element(self.item_to_order).text

    def get_shipping_details(self):
        pdb.set_trace()
        return self.find_element(self.name).get_attribute('value')

    def get_email(self):
        pdb.set_trace()
        return self.find_element(self.email).get_attribute('value')

    def empty_cart(self):
        self.find_element(self.delete_item).click()
        return OrderPage(self.driver)

    def is_empty(self):
        return self.find_element(self.select_product_button).text

    def logout(self):
        ac(self.driver).move_to_element(self.avatar).click().move_to_element(self.logout_link).click()
        return BasePage(self.driver)
