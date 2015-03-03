from objectsmap.locators import JsonTree
from pages.base_page import BasePage

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class IndexPageAuthorized(BasePage):
    TITLE = "JSON reader"
    LOCATION = "http://localhost/CustomHandlersModules/"

    def open(self):
        self._driver.get(IndexPageAuthorized.LOCATION)

    def loadJson(self):
        wait = WebDriverWait(self._driver, 10)
        try:
            wait.until(EC.presence_of_element_located(JsonTree.LOAD_BUTTON)).click()
            return True
        except TimeoutException:
            return False

    def clickTextTab(self):
        wait = WebDriverWait(self._driver, 10)
        try:
            wait.until(EC.element_to_be_clickable(JsonTree.JSON_TEXT_TAB)).click()
            return True
        except TimeoutException:
            return False

    def clickTreeTab(self):
        wait = WebDriverWait(self._driver, 20)
        try:
            wait.until(EC.element_to_be_clickable(JsonTree.JSON_TREE_TAB)).click()
            return True
        except TimeoutException:
            return False

    def ifTextPresent(self):
        wait = WebDriverWait(self._driver, 10)
        try:
            wait.until(EC.presence_of_element_located(JsonTree.TEXT_AREA))
            return True
        except TimeoutException:
            return False

    def getText(self):
        wait = WebDriverWait(self._driver, 10)
        try:
            return wait.until(EC.presence_of_element_located(JsonTree.TEXT_AREA)).getText()
        except TimeoutException:
            return None

    def getBranches(self):
        return self._driver.find_elements(JsonTree.LI_BRANCH)

    def clickBranch(self, index):
        try:
            self.getBranches()[index].click()
            return True
        except:
            return False