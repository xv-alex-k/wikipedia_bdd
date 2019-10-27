from selenium.webdriver.common.by import By

from features.pages.base_page import BasePage


class LoginPage(BasePage):
    FIELD_USERNAME = (By.ID, "wpName1")
    FIELD_PASSWORD = (By.ID, "wpPassword1")
    BUTTON_LOGIN = (By.ID, "wpLoginAttempt")

    def enter_username(self, username):
        self.type_in(self.FIELD_USERNAME, username)

    def enter_password(self, password):
        self.type_in(self.FIELD_PASSWORD, password)

    def click_login_button(self):
        self.click_on(self.BUTTON_LOGIN)
