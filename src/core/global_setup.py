from src.core.constants.selenium_constants import APPLICATION_URL
from src.core.driver.driver_manager import DriverManager


class GlobalSetup:

    def __init__(self):
        self.driver = None
        self.driver_manager = DriverManager()

    def init(self):
        self.driver = self.driver_manager.setup_driver()
        self.driver.get(APPLICATION_URL)

    def tear_down(self):
        self.driver.quit()


if __name__ == "__main__":
    global_setup = GlobalSetup()
    global_setup.init()
