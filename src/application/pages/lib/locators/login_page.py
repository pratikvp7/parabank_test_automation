from selenium.webdriver.common.by import By


class LoginPageLocators:

    def __init__(self, driver, log):
        self.driver = driver
        self.log = log

    def customer_login_text(self, locator_only=False):
        self.log.info("Finding 'Customer Login' text.")
        locator = By.XPATH, '//h2[text()="Customer Login"]'
        return str(locator) if locator_only else self.driver.find_element(*locator)

    def forgot_login_info_link(self, locator_only=False):
        self.log.info("Finding 'Forgot login info' link.")
        locator = (By.LINK_TEXT, 'Forgot Password?')
        return str(locator) if locator_only else self.driver.find_element(*locator)

    def login_button(self, locator_only=False):
        self.log.info("Finding 'login' button.")
        locator = (By.XPATH, "//button[@type='submit']")
        return str(locator) if locator_only else self.driver.find_element(*locator)

    def page_header(self, locator_only=False):
        self.log.info("Finding page header 'ParaBank'.")
        locator = By.XPATH, '//img[@title="ParaBank"]'
        return str(locator) if locator_only else self.driver.find_element(*locator)

    def password_field(self, locator_only=False):
        self.log.info("Finding 'password' field.")
        locator = By.NAME, 'password'
        return str(locator) if locator_only else self.driver.find_element(*locator)

    def register_link(self, locator_only=False):
        self.log.info("Finding 'Register' link.")
        locator = (By.XPATH, '//a[text()="Register"]')
        return str(locator) if locator_only else self.driver.find_element(*locator)

    def sub_header(self, locator_only=False):
        self.log.info("Finding page sub header 'Experience the difference'.")
        locator = (By.XPATH, "//p[text()='Experience the difference']")
        return str(locator) if locator_only else self.driver.find_element(*locator)

    def username_field(self, locator_only=False):
        self.log.info('Finding username field.')
        locator = By.NAME, 'username'
        return str(locator) if locator_only else self.driver.find_element(*locator)


