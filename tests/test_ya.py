# -*- coding: utf-8 -*-
from utils.conftest import *
from utils.base_page import *

URL = 'https://market.yandex.ru'


@pytest.mark.parametrize('user_name, password', parameters())
def test_market(browser, user_name, password):
    browser.maximize_window()
    browser.get(URL)
    start_page = StartPage(browser)
    start_page.take_screenshot('screenshots/1.png')
    login_page = start_page.set_region(region=u'Москва').login()
    home_page = login_page.enter_username(user_name).enter_password(password).sign_in()
    assert home_page.is_loaded()
    login_page.take_screenshot('screenshots/2.png')
    results_page = home_page.search('iphone 7 128Gb').expand_results()
    result = results_page.order_on_market().sort_by_price().get_first_result()
    results_page.take_screenshot('screenshots/3.png')
    assert 'Apple iPhone 7 128' in result.text
    product_detail_page = results_page.get_product_details()
    product_detail_page.take_screenshot('screenshots/4.png')
    cart_page = product_detail_page.add_to_cart().go_to_cart()
    cart_page.take_screenshot('screenshots/5.png')
    assert 'iPhone 7 128' in cart_page.product_in_cart()
    order_page = cart_page.place_order()
    assert 'iPhone 7 128' in order_page.get_order_details()
    assert 'yandex test' in order_page.get_shipping_details()
    assert 'email@yandex.ru' in order_page.get_email()
    order_page.take_screenshot('screenshots/6.png')
    order_page.empty_cart().logout()
    order_page.take_screenshot('screenshots/7.png')
