from behave import *
from pages.index_page import IndexPage

@given('first page of the web site')
def step_open(context):
    context.page = IndexPage(context.driver)
    context.page.open()

@when('user click enter reference and then enter his login and password')
def step_login(context):
    context.page.login("admin", "qwerty")

@then('user has authorized and logout reference appeared')
def step_assert(context):
    assert context.page.logoutPresence(120)