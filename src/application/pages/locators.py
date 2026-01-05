from src.application.pages.lib.locators.login_page import LoginPageLocators


class Locators:

    def __init__(self, driver, log):
        self.log = log
        self.driver = driver

        self.login_page = LoginPageLocators(self.driver, self.log)

