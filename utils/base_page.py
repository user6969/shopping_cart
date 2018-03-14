# -*- coding: utf-8 -*-
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from utils.locators import *
from time import sleep


TIME_OUT = 10


class BasePage(object):

    def __init__(self, browser):
        self.driver = browser
        self.wait = WebDriverWait(browser, TIME_OUT)

    def find_element(self, locator):
        try:
            return self.driver.find_element(*locator)
        except (NoSuchElementException, TimeoutException):
            return self.wait.until(ec.presence_of_element_located(locator))

    def find_elements(self, locator):
        return self.wait.until(ec.presence_of_all_elements_located(locator))

    def element_clickable(self, locator):
        try:
            return self.wait.until(ec.element_to_be_clickable(locator))
        except TimeoutException:
            return None
        finally:
            pass #TODO

    def element_visible(self, locator):
        try:
            return self.wait.until(ec.visibility_of_element_located(locator))
        except TimeoutException:
            return None
        finally:
            pass #TODO

    def take_screenshot(self, file_name):
        return self.driver.save_screenshot(file_name)


class StartPage(BasePage):

    def __init__(self, driver):
        super(StartPage, self).__init__(driver)

    def set_region(self, region):
        self.find_element(StartPageLocators.change_city).click()
        self.find_element(StartPageLocators.new_city).send_keys(region + '\n')
        self.find_element(StartPageLocators.new_city).send_keys(Keys.ENTER)
        self.find_element(StartPageLocators.go_button).click()
        return StartPage(self.driver)

    def login(self):
        sleep(2)
        self.find_element(StartPageLocators.login_button).click()
        windows = self.driver.window_handles
        self.driver.switch_to_window(windows[1])
        return LoginPage(self.driver)


class LoginPage(BasePage):

    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)

    def enter_username(self, username):
        self.find_element(LoginPageLocators.username).send_keys(username)
        return LoginPage(self.driver)

    def enter_password(self, password):
        self.find_element(LoginPageLocators.password).send_keys(password)
        return LoginPage(self.driver)

    def sign_in(self):
        self.find_element(LoginPageLocators.login_button).click()
        windows = self.driver.window_handles
        self.driver.switch_to_window(windows[0])
        return HomePage(self.driver)


class HomePage(BasePage):

    def __init__(self, driver):
        super(HomePage, self).__init__(driver)

    def is_loaded(self):
        try:
            self.find_element(HomePageLocators.avatar)
            return True
        except NoSuchElementException:
            return False

    def search(self, item):
        self.find_element(HomePageLocators.search_field).send_keys(item)
        self.find_element(HomePageLocators.search_button).click()
        return ResultsPage(self.driver)


class ResultsPage(BasePage):

    def __init__(self, driver):
        super(ResultsPage, self).__init__(driver)

    def expand_results(self):
        self.find_element(ResultsPageLocators.expand_results_link).click()
        return ResultsPage(self.driver)

    def order_on_market(self):
        self.find_element(ResultsPageLocators.order_on_market_tick_box).click()
        return ResultsPage(self.driver)

    def sort_by_price(self):
        self.find_element(ResultsPageLocators.sort_by_price_filter).click()
        return ResultsPage(self.driver)

    def get_first_result(self):
        return self.find_element(ResultsPageLocators.first_result)

    def get_product_details(self):
        sleep(2)
        self.element_clickable(ResultsPageLocators.first_result)
        self.find_element(ResultsPageLocators.first_result).click()
        return ProductPage(self.driver)


class ProductPage(BasePage):

    def __init__(self, driver):
        super(ProductPage, self).__init__(driver)

    def add_to_cart(self):
        self.find_element(ProductPageLocators.to_cart).click()
        return ProductPage(self.driver)

    def go_to_cart(self):
        self.find_element(ProductPageLocators.go_to_cart_button).click()
        return CartPage(self.driver)


class CartPage(BasePage):

    def __init__(self, driver):
        super(CartPage, self).__init__(driver)

    def product_in_cart(self):
        self.element_visible(CartPageLocators.item_to_purchase)
        return self.find_element(CartPageLocators.item_to_purchase).text

    def place_order(self):
        self.find_element(CartPageLocators.place_order_button).click()
        return OrderPage(self.driver)


class OrderPage(BasePage):

    def __init__(self, driver):
        super(OrderPage, self).__init__(driver)

    def get_order_details(self):
        return self.find_element(OrderPageLocators.item_to_order).text

    def get_shipping_details(self):
        self.element_visible(OrderPageLocators.name)
        return self.find_element(OrderPageLocators.name).get_attribute('value')

    def get_email(self):
        self.element_visible(OrderPageLocators.email)
        return self.find_element(OrderPageLocators.email).get_attribute('value')

    def empty_cart(self):
        sleep(2)
        self.find_element(OrderPageLocators.delete_item).click()
        return OrderPage(self.driver)

    def is_empty(self):
        return self.find_element(OrderPageLocators.select_product_button).text

    def logout(self):
        self.find_element(OrderPageLocators.avatar).click()
        self.find_element(OrderPageLocators.logout_link).click()
        return BasePage(self.driver)
