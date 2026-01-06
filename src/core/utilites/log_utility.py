import datetime

from src.core.utilites.directory_handler import DirectoryHandler


class LogUtility:
    def __init__(self):
        self.dir_handler = DirectoryHandler()

    def info(self, msg):
        current_data_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{current_data_time} [INFO] {msg}")

    def debug(self, msg):
        current_data_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{current_data_time} [DEBUG] {msg}")

    def warn(self, msg):
        current_data_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{current_data_time} [WARN] {msg}")

    def error(self, msg):
        current_data_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{current_data_time} [ERROR] {msg}")

    def space(self):
        print("\n")

    def __write_log(self, log_level, msg):
        current_data_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{current_data_time} [{log_level}] {msg}")


if __name__ == '__main__':
    log = LogUtility()
    log.info("Hello")
    log.debug("Hello")
    log.warn("Hello")
    log.error("Hello")
