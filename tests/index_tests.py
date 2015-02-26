import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.index_page import IndexPage
from pages.index_page_authorized import IndexPageAuthorized

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

def test_auth_incorrect(driver):
    index_page = IndexPage(driver)
    index_page.open()
    index_page.login("admin", "dsfsdf")
    assert not index_page.ifLogoutPresent(10)

def test_auth_correct(driver):
    index_page = IndexPage(driver)
    index_page.open()
    index_page.login("admin", "qwerty")
    assert index_page.ifLogoutPresent(120)

def test_refresh(driver):
    index_page = IndexPage(driver)
    index_page.open()
    driver.refresh()
    assert index_page.ifLogoutPresent(10)

def test_loadJson(driver):
    index_page = IndexPageAuthorized(driver)
    index_page.open()
    index_page.loadJson()
    index_page.clickTreeTab()
    index_page.clickTextTab()
    assert index_page.ifTextPresent()

def test_branches(driver):
    index_page = IndexPageAuthorized(driver)
    index_page.open()
    index_page.loadJson()
    index_page.clickTreeTab()
    res = index_page.clickBranch(0)
    assert res