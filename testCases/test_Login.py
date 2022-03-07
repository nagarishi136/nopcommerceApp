import time
import os
import pytest
from selenium import webdriver

import utilities.datetime
from Config.config import TestData
from PageObjects.LoginPage import  LoginPage
#from utilities.readProperties import ReadConfig
from utilities.datetime import current_date_time
from utilities.customLogger import LogGen
class Test_001_Login():
    BASE_URL=TestData.URL
    USER_NAME=TestData.EMAIL
    PASSWORD=TestData.PASSWORD_NOPCOMMERACE
    logger=LogGen.loggen()

    def test_HomePage_Title(self):
        self.logger.info("************************** Test_001_Login IS STARTED ****************************")
        self.logger.info("************************** VERIFY THE HomePage_Title ****************************")

        self.driver=webdriver.Chrome(TestData.CHROME_EXECUTABLE_PATH)
        self.driver.get(self.BASE_URL)
        act_title=self.driver.title

        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("**************************  HomePage_Title IS PASSED ****************************")


        else:
            #self.driver.get_screenshot_as_file("test_homepage.png")
            self.driver.save_screenshot(".\\Screenshots\\"+"test_HomePage_Title"+utilities.datetime.current_date_time()+".png")
            self.driver.close()
            self.logger.info("**************************  HomePage_Title IS FAILED ****************************")

            assert False
    def test_login(self):
        self.logger.info("************************** Test_001_Login IS STARTED ****************************")
        self.logger.info("************************** VERIFY THE LOGIN PAGE ****************************")

        self.driver = webdriver.Chrome(TestData.CHROME_EXECUTABLE_PATH)
        self.driver.get(self.BASE_URL)
        self.LoginPage=LoginPage(self.driver)
        self.LoginPage.setUserName(self.USER_NAME)
        self.LoginPage.setPassword(self.PASSWORD)
        self.LoginPage.clickLogin()

        act_title =self.driver.title

        if act_title == "Dashboard / nopCommerce administration":

            assert True
            self.driver.close()
            self.logger.info("**************************  LOGINPAGE IS PASSED ****************************")


        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_login"+utilities.datetime.current_date_time()+".png")
            self.driver.close()
            assert False
            self.logger.info("**************************  LOGINPage IS FAILED ****************************")


