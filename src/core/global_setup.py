from src.core.common.driver_constants import EDGE
from src.core.driver.driver_manager import DriverManager


class GlobalSetup:

    def __init__(self):
        self.driver = None
        self.driver_manager = DriverManager()

    def init(self):
         self.driver = self.driver_manager.setup_driver()
         self.driver.get("https://www.google.com")


if __name__ == "__main__":
    global_setup = GlobalSetup()
    global_setup.init()

