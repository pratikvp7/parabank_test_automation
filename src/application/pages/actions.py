from src.application.pages.lib.actions.login_page import LoginPageActions


class Actions:

    def __init__(self, driver, log):
        self.log = log
        self.driver = driver

        self.login_page = LoginPageActions(self.log, self.driver)
