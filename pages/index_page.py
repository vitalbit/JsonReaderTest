from objectsmap.locators import Login
from pages.base_page import BasePage
from pages.exceptions import LoginException

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class IndexPage(BasePage):
    TITLE = "JSON reader"
    LOCATION = "http://localhost/CustomHandlersModules/"

    def logoutPresence(self, timeToWait):
        try:
            WebDriverWait(self._driver, timeToWait).until(EC.presence_of_element_located(Login.EXIT_MENU))
            return True
        except TimeoutException:
            return False

    def isIndexPage(self):
        return self._driver.title == IndexPage.TITLE

    def open(self):
        self._driver.get(IndexPage.LOCATION)

    def login(self, name, password):
        wait = WebDriverWait(self._driver, 10)
        try:
            wait.until(EC.presence_of_element_located(Login.ENTER_MENU)).click()
            wait.until(EC.presence_of_element_located(Login.LOGIN_TEXT)).send_keys(name)
            wait.until(EC.presence_of_element_located(Login.PASSWORD_TEXT)).send_keys(password)
            wait.until(EC.presence_of_element_located(Login.SUBMIT_BUTTON)).click()
        except TimeoutException:
            raise LoginException('Something wrong with user login!')