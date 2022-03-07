import time

from Config.config import TestData
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest
from selenium.common.exceptions import TimeoutException


class Test_Home(BaseTest):

    def test_home_page_login(self):
        self.LoginPage = LoginPage(self.driver)
        self.LoginPage.do_invalid_Login(TestData.USER_NAME, TestData.INVALID_PASSWORD)

    def test_home_page_text(self):
        self.LoginPage = LoginPage(self.driver)
        homePage = self.LoginPage.do_invalid_Login(TestData.USER_NAME, TestData.INVALID_PASSWORD)
        time.sleep(5)

        self.driver.set_page_load_timeout(50)
        invalid_text = homePage.get_text_name()

        print(invalid_text)
        assert  invalid_text == TestData.INVALID_TEXT,"The password that you've entered is incorrect.?"
