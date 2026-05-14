

class WaitActions:

    def __int__(self, driver, log):
        self.driver = driver
        self.log = log

    def wait_until_displayed(self, retry=2):
        self.log.info("Waiting until element is displayed.")
        pass

