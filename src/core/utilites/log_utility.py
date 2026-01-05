import datetime
import os

from root import ROOT_DIR
from src.core.utilites.directory_handler import DirectoryHandler


class LogUtility:
    def __init__(self):
        self.current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.dir_handler = DirectoryHandler()

    def info(self, msg):
        print(f"{self.current_time} [INFO] {msg}")

    def debug(self, msg):
        print(f"{self.current_time} [DEBUG] {msg}")

    def warn(self, msg):
        print(f"{self.current_time} [WARN] {msg}")

    def error(self, msg):
        print(f"{self.current_time} [ERROR] {msg}")

    def space(self):
        print("\n")

    def __write_log(self, log_level, msg):
        print(f"{self.current_time} [{log_level}] {msg}")


if __name__ == '__main__':
    log = LogUtility()
    log.info("Hello")
    log.debug("Hello")
    log.warn("Hello")
    log.error("Hello")
