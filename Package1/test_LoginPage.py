import time

import pytest

from Config.config import TestData
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest

class Test_Login(BaseTest):







     def test_get_total_info_IND_team(self):
         self.LoginPage = LoginPage(self.driver)
         self.LoginPage.do_fide_task()
         print(self.LoginPage.get_length_rows())

         assert self.LoginPage.get_length_rows() ==101

         self.LoginPage.get_Total_info()
    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
     def test_current_tournaments(self):
         self.LoginPage = LoginPage(self.driver)
         self.LoginPage.do_fide_task()
         self.LoginPage.get_tournaments()
         self.LoginPage.click_on_country_drop_down()
         time.sleep(4)
         self.LoginPage.enter_text_drop_down(TestData.TOURNMENT_TEXT)
         time.sleep(5)
         self.LoginPage.select_item(TestData.TOURNMENT_TEXT_ITEM)
         time.sleep(5)
         self.LoginPage.select_Current_and_future_periods()
         time.sleep(5)









