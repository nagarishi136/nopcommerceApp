import pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service

from Config.config import TestData
from Pages.LoginPage import LoginPage
from Tests.test_Valid_Credentials import Test_Valid_Credentials
from Tests.test_InValid_Credentials import Test_InValid_Credentials
from Tests.test_fide import Test_Fide
@pytest.yield_fixture()
def setup():
      print("Opening url to login")
      yield
      print("closing browsier after login")

def test_valid_Login(self,setup):
          self.LoginPage=LoginPage(self.driver)
          self.LoginPage.do_valid_Login(TestData.USER_NAME,TestData.VALID_PASSWORD)


def test_Invalid_Login(self,setup):
      self.LoginPage = LoginPage(self.driver)
      self.LoginPage.do_invalid_Login(TestData.USER_NAME, TestData.INVALID_PASSWORD)

def test_Login_Page(self,setup):
            global driver
            s = Service(r"C:\Users\Nagamalla Reddy-2639\drivers\chromedriver.exe")
            driver = webdriver.Chrome(service=s)
            driver.maximize_window()
            driver.implicitly_wait(5)
            driver.set_page_load_timeout(50)
            # Open the FIDE website
            driver.get('https://www.fide.com/')



