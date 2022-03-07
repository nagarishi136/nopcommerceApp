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
from utilities import  XLUtils
class Test_002_DDT_Login():
    BASE_URL=TestData.URL
    path=".\\TestData\\nopcommerce admin.xlsx"

    logger=LogGen.loggen()


    def test_login_ddt(self):
        self.logger.info("************************** Test_002_Login IS STARTED ****************************")
        self.logger.info("************************** VERIFY THE LOGIN DDT PAGE ****************************")

        self.driver = webdriver.Chrome(TestData.CHROME_EXECUTABLE_PATH)
        self.driver.get(self.BASE_URL)

        self.LoginPage=LoginPage(self.driver)
        self.rows=XLUtils.getRowCount(self.path,"login")
        print("Number of rows --->",self.rows)
        for r in range(2,self.rows+1):
            self.username1=XLUtils.readData(self.path,'login',r,1)
            self.password1=XLUtils.readData(self.path,'login',r,2)
            self.exp=XLUtils.readData(self.path,'login',r,3)




            self.LoginPage.setUserName(self.username1)
            self.LoginPage.setPassword(self.password1)
            self.LoginPage.clickLogin()
            time.sleep(5)


            act_title =self.driver.title
            exp_title="Dashboard / nopCommerce administration"

        if act_title == exp_title:
            print("login is success")
            assert True
            self.driver.close()
            self.logger.info("**************************  LOGINPAGE IS PASSED ****************************")


        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_login"+utilities.datetime.current_date_time()+".png")
            self.driver.close()
            assert False
            self.logger.info("**************************  LOGINPage IS FAILED ****************************")


