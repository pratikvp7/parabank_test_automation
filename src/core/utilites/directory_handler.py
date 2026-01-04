import os

from root import ROOT_DIR
from src.core.constants.driver_constants import *


class DirectoryHandler:
    def __init__(self):
        self.root_dir = ROOT_DIR

        self.DATA_PATH = os.path.join(self.root_dir, SRC_DIR, APPLICATION_DIR, DATA_DIR)
        os.makedirs(DATA_PATH, exist_ok=True)

        self.REPORT_PATH = os.path.join(self.DATA_PATH, REPORT_DIR)
        os.makedirs(self.REPORT_PATH, exist_ok=True)


if __name__ == '__main__':
    directory_handler = DirectoryHandler()
