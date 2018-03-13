import pytest
from selenium import webdriver


@pytest.yield_fixture(scope='session')
def browser():
    options = webdriver.ChromeOptions()
    #options.add_argument("--kiosk")
    #driver = webdriver.Chrome(chrome_options=options)
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
