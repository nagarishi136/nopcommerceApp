import time

import pytest
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException,ElementNotInteractableException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest


class Test_Makemy_Trip(BaseTest):

    def test_MakeMy_Trip(self):
        self.HomePage = HomePage(self.driver)
        self.HomePage.get_makemy_Trip_Login(TestData.FROM_PLACE,TestData.TO_PLACE)
        print(self.HomePage.get_Count_Of_flights())

        assert self.HomePage.get_Count_Of_flights() != [],"Number of Flights are not 7"

        self.driver.execute_script("window.scrollBy(0,200)", "")
        self.HomePage.get_makemy_Trip_Flight_Names()



