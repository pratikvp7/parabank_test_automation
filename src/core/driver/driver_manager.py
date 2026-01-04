from src.core.constants.driver_constants import *
from selenium import webdriver


class DriverManager:

    def __init__(self):
        self.driver = None

    def setup_driver(self, browser=CHROME):
        self.driver = self.__connect_selenium_server(browser)
        self.driver.implicitly_wait(IMPLICIT_WAIT)
        self.driver.set_page_load_timeout(WEB_PAGE_LOAD_TIMEOUT)
        return self.driver


    def __connect_selenium_server(self, browser, max_retry=10):
        try:
            for retry in range(max_retry):
                if browser == CHROME:
                    return webdriver.Chrome()
                if browser == EDGE:
                    return webdriver.Edge()
                if browser == SAFARI:
                    return webdriver.Safari()
        except:
            raise Exception("Failed to connect selenium server...")
