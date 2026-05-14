

class PageActions:

    def __init__(self, driver, log):
        self.driver = driver
        self.log = log

    def refresh_page(self):
        self.log.info("Refreshing the page.")
        self.driver.refresh()

