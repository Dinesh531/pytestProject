from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):

    txt_username = (By.ID, "username")
    txt_password = (By.ID, "password")
    btn_login = (By.XPATH, "//button[text()='Login']")
    msg_error = (By.ID, "flash")

    def login(self, username, password):

        self.type(self.txt_username, username)
        self.type(self.txt_password, password)
        self.click(self.btn_login)

    def get_error_message(self):
        return self.get_text(self.msg_error)