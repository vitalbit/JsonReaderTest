from selenium.webdriver.common.by import By

class Login:
    ENTER_MENU = (By.ID, 'enter')
    LOGIN_TEXT = (By.ID, 'login')
    PASSWORD_TEXT = (By.ID, 'password')
    SUBMIT_BUTTON = (By.ID, 'subm_button')
    EXIT_MENU = (By.ID, 'exit')

class JsonTree:
    LOAD_BUTTON = (By.ID, 'load_json')
    JSON_TEXT_TAB = (By.ID, 'json_text')
    JSON_TREE_TAB = (By.ID, 'json_tree')
    LI_BRANCH = (By.ID, 'li_branch')
    TEXT_AREA = (By.ID, 'text_area')