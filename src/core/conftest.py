import pytest
from src.core.global_setup import GlobalSetup

#  Decorators
test_id = pytest.mark.test_id
severity = pytest.mark.severity
description = pytest.mark.description


# @pytest.fixture(scope="session", autouse=True)
# def startup_routine(request):
#     print("[START] Starting up...]")
#     global_setup = GlobalSetup()
#     global_setup.init()
#     yield
#     global_setup.tear_down()
#     print("[END] All done...]")
