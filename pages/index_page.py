from objectsmap.locators import Login
from pages.base_page import BasePage

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class IndexPage(BasePage):
    TITLE = "JSON reader"
    LOCATION = "http://localhost/CustomHandlersModules/"

    def ifLogoutPresent(self, timeToWait):
        try:
            WebDriverWait(self._driver, timeToWait).until(EC.presence_of_element_located(Login.Exit_Menu))
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
            wait.until(EC.presence_of_element_located(Login.Enter_Menu)).click()
            wait.until(EC.presence_of_element_located(Login.Login_Text)).send_keys(name)
            wait.until(EC.presence_of_element_located(Login.Password_Text)).send_keys(password)
            wait.until(EC.presence_of_element_located(Login.Submit_Button)).click()
            return True
        except TimeoutException:
            return False