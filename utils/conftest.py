import pytest
from selenium import webdriver


@pytest.yield_fixture(scope='session')
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
