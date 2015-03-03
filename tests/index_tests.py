import pytest
from selenium import webdriver

from pages.index_page import IndexPage
from pages.index_page_authorized import IndexPageAuthorized

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
    assert not index_page.logoutPresence(10)

def test_auth_correct(driver):
    index_page = IndexPage(driver)
    index_page.open()
    index_page.login("admin", "qwerty")
    assert index_page.logoutPresence(120)

def test_refresh(driver):
    index_page = IndexPage(driver)
    index_page.open()
    driver.refresh()
    assert index_page.logoutPresence(10)

def test_loadJson(driver):
    index_page = IndexPageAuthorized(driver)
    index_page.open()
    index_page.loadJson()
    index_page.clickTreeTab()
    index_page.clickTextTab()
    assert index_page.textPresence()

def test_branches(driver):
    index_page = IndexPageAuthorized(driver)
    index_page.open()
    index_page.loadJson()
    index_page.clickTreeTab()
    index_page.clickBranch(0)