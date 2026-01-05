from src.application.pages.lib.events.login_page import LoginPageEvents


class Events:

    def __init__(self, driver, log):
        self.log = log
        self.driver = driver

        self.login_page = LoginPageEvents(self.log, self.driver)


