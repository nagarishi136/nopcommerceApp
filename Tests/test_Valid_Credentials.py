import time

import pytest

from Config.config import TestData
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest

class Test_Valid_Credentials(BaseTest):


     def test_valid_Login(self):
          self.LoginPage=LoginPage(self.driver)
          self.text=self.LoginPage.do_valid_Login(TestData.USER_NAME,TestData.VALID_PASSWORD)



