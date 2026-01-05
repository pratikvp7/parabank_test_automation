from src.application.pages.actions import Actions
from src.core.global_setup import GlobalSetup


class TestSmoke:

    @staticmethod
    def setup_class(cls):
        cls.global_setup = GlobalSetup()
        cls.log = cls.global_setup.log
        cls.global_setup.init()
        cls.driver = cls.global_setup.driver

        cls.actions = Actions(cls.log, cls.driver)

    @staticmethod
    def teardown_class(cls):
        cls.global_setup.tear_down()

    def test_header(self):
        title_result = self.actions.login_page.is_parabank_title_displayed()
        assert title_result

    def test_login_page(self):
        login_page_result = self.actions.login_page.is_customer_login_text_displayed()
        assert login_page_result

        username_result = self.actions.login_page.is_username_field_displayed()
        assert username_result

        password_result = self.actions.login_page.is_password_field_displayed()
        assert password_result

