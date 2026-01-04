import pytest

from src.core.global_setup import GlobalSetup


@pytest.fixture(scope="session", autouse=True)
def startup_routine():
    print("[START] Starting up...]")
    global_setup = GlobalSetup()
    global_setup.init()
    yield
    global_setup.tear_down()
    print("[END] All done...]")
