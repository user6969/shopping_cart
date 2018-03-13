# -*- coding: utf-8 -*-
import pytest
from utils.conftest import *
from utils.base_page import *

URL = 'https://market.yandex.ru'


def test_market(browser):
    browser.maximize_window()
    browser.get(URL)
    start_page = BasePage(browser)
    login_page = start_page.set_region(region='Moscow').login()
    home_page = login_page.enter_username('yan.dextest@yandex.ru').enter_password('w3bm@ster1').sign_in()
    assert home_page.is_loaded()
    results_page = home_page.search('iphone 7 128Gb').expand_results()
    result = results_page.order_on_market().sort_by_price().get_first_result()
    assert 'Apple iPhone 7 128G' in result.text
    product_detail_page = results_page.get_product_details()
    cart_page = product_detail_page.add_to_cart().go_to_cart()
    assert 'iPhone 7 128Gb' in cart_page.product_in_cart()
    order_page = cart_page.place_order()
    assert 'iPhone 7 128Gb' in order_page.get_order_details()
    assert 'yan dex' in order_page.get_shipping_details()
    assert 'yan.dextest@yandex.ru' in order_page.get_email()
    order_page.empty_cart().logout()
