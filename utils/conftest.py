import pytest
import csv
from selenium import webdriver

TEST_DATA = 'test_data.csv'


@pytest.yield_fixture(scope='session')
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture()
def parameters():
    params = []
    with open(TEST_DATA, 'rb') as data_file:
        data = csv.reader(data_file)
        for row in data:
            params.append(tuple(row))
    return params
