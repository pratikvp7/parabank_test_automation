from src.application.pages.lib.actions.login_page import LoginPageActions


class LoginPageEvents:

    def __init__(self, driver, log):
        self.driver = driver
        self.log = log

        self.login_actions = LoginPageActions(self.log, self.driver)

    def Login_routine(self, username, password):
        self.log.info("Performing login routine...")
        self.login_actions.input_username(username)
        self.login_actions.input_password(password)
        self.login_actions.click_login_button()
