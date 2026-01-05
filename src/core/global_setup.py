from src.core.constants.selenium_constants import APPLICATION_URL
from src.core.driver.driver_manager import DriverManager
from src.core.utilites.log_utility import LogUtility


class GlobalSetup:

    def __init__(self):
        self.driver = None
        self.log = LogUtility()
        self.driver_manager = DriverManager(self.log)

    def init(self):
        self.log.info("Initializing Global Setup")
        self.driver = self.driver_manager.setup_driver()
        self.driver.get(APPLICATION_URL)

    def tear_down(self):
        self.log.info("Tearing down Global Setup")
        self.driver.quit()


if __name__ == "__main__":
    global_setup = GlobalSetup()
    global_setup.init()
