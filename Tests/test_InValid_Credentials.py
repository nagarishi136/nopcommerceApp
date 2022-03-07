import time

import pytest

from Config.config import TestData
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest

class Test_InValid_Credentials(BaseTest):


      def test_Invalid_Login(self):
          self.LoginPage=LoginPage(self.driver)


          self.text_mgs=self.LoginPage.do_invalid_Login(TestData.USER_NAME,TestData.INVALID_PASSWORD)

          assert self.text_mgs != "" ,'Your data is  incorrect'


