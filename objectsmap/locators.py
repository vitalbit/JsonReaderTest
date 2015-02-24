from selenium.webdriver.common.by import By

class Login:
    Enter_Menu = (By.ID, 'enter')
    Login_Text = (By.ID, 'login')
    Password_Text = (By.ID, 'password')
    Submit_Button = (By.ID, 'subm_button')
    Exit_Menu = (By.ID, 'exit')

class JsonTree:
    Load_Button = (By.ID, 'load_json')
    Json_Text_Tab = (By.ID, 'json_text')
    Json_Tree_Tab = (By.ID, 'json_tree')
    Li_Branch = (By.ID, 'li_branch')