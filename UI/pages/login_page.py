from UI.locators.basic_locators import *
from UI.pages.base_page import BasePage


class LoginPage(BasePage):
    def login(self, login, password):
        self.click(locator=LocatorsLoginPage.LOCATOR_LOGIN)
        self.send_keys(locator=LocatorsLoginPage.LOCATOR_INPUT_LOGIN, send_input=login)
        self.send_keys(locator=LocatorsLoginPage.LOCATOR_INPUT_PASSWORD, send_input=password)
        self.click(locator=LocatorsLoginPage.LOCATOR_BUTTON_CONTINUE)
