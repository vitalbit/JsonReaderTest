import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.index_page import IndexPage

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope='module')
def driver(request):
    _driver = webdriver.Firefox()

    def close():
        _driver.quit()

    request.addfinalizer(close)
    return _driver

def test_title(driver):
    index_page = IndexPage(driver)
    index_page.open()
    assert index_page.isIndexPage()

def test_auth(driver):
    index_page = IndexPage(driver)
    index_page.open()
    assert index_page.login("admin", "qwerty")