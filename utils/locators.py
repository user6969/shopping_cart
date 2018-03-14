# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By


class StartPageLocators(object):
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


class LoginPageLocators(object):
    username = (By.NAME, 'login')
    password = (By.NAME, 'passwd')
    login_button = (By.CSS_SELECTOR, 'span.passport-Button-Text')


class HomePageLocators(object):
    avatar = (By.CSS_SELECTOR, 'span.user__icon')
    search_field = (By.ID, 'header-search')
    search_button = (By.CSS_SELECTOR, 'button.button2')


class ResultsPageLocators(object):
    xpath_expand_search = '//div[1]/div[3]/div/div/div/div[1]/a'
    xpath_order_on_market = '//*[@id="search-prepack"]/div/div/div[2]/div/div[1]/div[3]/fieldset/div[1]/label/div/span'
    xpath_order_by_price = '//div[1]/div[4]/div[1]/div[2]/div[1]/div[1]/div[3]/a'
    xpath_first_result = '//div[1]/div[4]/div[2]/div[1]/div[2]/div/div[1]/div/div[4]/div[1]/div/a'

    expand_results_link = (By.XPATH, xpath_expand_search)
    order_on_market_tick_box = (By.XPATH, xpath_order_on_market)
    sort_by_price_filter = (By.XPATH, xpath_order_by_price)
    first_result = (By.XPATH, xpath_first_result)


class ProductPageLocators(object):
    xpath_add_to_cart = '//div[1]/div[4]/div[4]/div[3]/div/div/div/div[5]/div/a'
    xpath_go_to_card = '//div[3]/div/div/div[1]/div[1]/div/div/div/div[1]/div[2]/div[1]/a/span[2]'

    to_cart = (By.CSS_SELECTOR, 'a.b-zone_js_inited')
    go_to_cart_button = (By.XPATH, xpath_go_to_card)


class CartPageLocators(object):
    xpath_item = '//div[1]/div[2]/div[1]/div[3]/div//div[2]/div//div[2]/div//div'
    xpath_place_order = '//div[1]/div[3]/div/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/button'
    item_to_purchase = (By.PARTIAL_LINK_TEXT, 'iPhone 7 128')
    place_order_button = (By.XPATH, xpath_place_order)


class OrderPageLocators(object):
    item_to_order = (By.CSS_SELECTOR, 'div.n-checkout-offer__item-name')
    name = (By.NAME, 'user-name')
    email = (By.NAME, 'user-email')
    delete_item = (By.CSS_SELECTOR, 'div.image.image_name_trash')
    select_product_button = (By.CSS_SELECTOR, 'div.n-w-checkout__text')
    avatar = (By.CSS_SELECTOR, '.n-passport-suggest-popup-opener > a:nth-child(1) > span:nth-child(1)')
    logout_link = (By.LINK_TEXT, u'Выйти')
