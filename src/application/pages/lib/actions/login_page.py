from selenium.common import NoSuchElementException

from src.application.pages.lib.locators.login_page import LoginPageLocators


class LoginPageActions:

    def __init__(self, driver, log):
        self.driver = driver
        self.log = log

        self.login_page_locators = LoginPageLocators(self.driver, self.log)

    def click_forgot_login_info_link(self):
        self.log.info("Clicking 'Forgot login info' link.")
        self.login_page_locators.forgot_login_info_link().click()

    def click_login_button(self):
        self.log.info("Clicking login button.")
        self.login_page_locators.login_button().click()

    def input_password(self, password):
        self.log.info(f"Inputting password: {password}.")
        self.login_page_locators.password_field().send_keys(password)

    def input_username(self, username):
        self.log.info(f"Inputting username: {username}.")
        self.login_page_locators.username_field().send_keys(username)

    def is_customer_login_text_displayed(self):
        self.log.info("Is 'Customer Login' text displayed?")
        try:
            return self.login_page_locators.customer_login_text().is_displayed()
        except NoSuchElementException:
            return False

    def is_login_page_displayed(self):
        self.log.info("Is login page is displayed?")
        try:
            return self.login_page_locators.login_button().is_displayed()
        except NoSuchElementException:
            return False

    def is_parabank_sub_title_displayed(self):
        self.log.info("Is Parabank sub title is displayed?")
        try:
            return self.login_page_locators.sub_header().is_displayed()
        except NoSuchElementException:
            return False

    def is_parabank_title_displayed(self):
        self.log.info("Is Parabank title is displayed?")
        try:
            return self.login_page_locators.page_header().is_displayed()
        except NoSuchElementException:
            return False

    def is_username_field_displayed(self):
        self.log.info("Is 'username' field displayed?")
        try:
            return self.login_page_locators.username_field().is_displayed()
        except NoSuchElementException:
            return False

    def is_password_field_displayed(self):
        self.log.info("Is 'password' field displayed?")
        try:
            return self.login_page_locators.password_field().is_displayed()
        except NoSuchElementException:
            return False
