import self as self

from Config.config import TestData
from Pages.BasePage import BasePage
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import NoSuchElementException




class HomePage(BasePage):
     """ LOGIN  PAGE LOCATORS FOR MAKEMY TRIP """
     POP_UP1=(By.XPATH,"//*[@id='root']/div/div[2]/div/main/div[9]/span")
     POP_UP2=(By.XPATH,'/html/body')
     FROM=(By.XPATH,"//span[text()='From']")
     #FROM_DATA_SEND_KEYS=(By.XPATH,"//input[@placeholder='From']")
     FROM_DATA_SEND_KEYS = (By.CSS_SELECTOR, "input[placeholder='From']")
     #FROM_DATA_CLICK=(By.XPATH,"//li[@id='react-autowhatever-1-section-0-item-0']")
     FROM_DATA_CLICK = (By.ID, 'react-autowhatever-1-section-0-item-0')
     # TO_DATA_SEND_KEYS=(By.XPATH,"//input[@autocomplete='off']")
     # TO_DATA_CLICK=(By.XPATH,"//li[@id='react-autowhatever-1-section-0-item-0']")
     TO_DATA_SEND_KEYS = (By.CSS_SELECTOR, "input[autocomplete='off']")
     TO_DATA_CLICK=(By.ID,'react-autowhatever-1-section-0-item-0')

     DEPARTURE_CLICK=(By.XPATH,"//div[@id='root']//div[3]/label/span")
     DEPARTURE_DATE_CLICK=(By.XPATH,"//*[@id='root']/div/div[2]/div/div/div[2]/div[1]/div[3]/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div[3]/div[1]/div[4]")
     #SEARECH_BUTTON_CLICK=(By.XPATH,"//a[@class='primaryBtn font24 latoBold widgetSearchBtn ']")
     SEARECH_BUTTON_CLICK = (By.CSS_SELECTOR, "a[class='primaryBtn font24 latoBold widgetSearchBtn ']")

     def __init__(self,driver):
          super().__init__(driver)
          self.driver.maximize_window()
          """ HOME PAGE LOCATORS FOR MAKEMY TRIP  """
     #FLIGHT_NAMES = (By.XPATH, "//span[@class='boldFont blackText airlineName']")
     FLIGHT_NAMES = (By.CSS_SELECTOR, "span[class='boldFont blackText airlineName']")
     START_TIME = (By.XPATH, "//div[contains(@class,'Left')]//p[contains(@class,'blackText')]")
     END_TIME = (By.XPATH, "//div[contains(@class,'Right')]//p[contains(@class,'hrtlCenter')]")

     def get_makemy_Trip_Login(self,key1,key2):
          self.driver.get(TestData.MAKEMYTRIP_URL)
          time.sleep(5)
          self.do_click(self.POP_UP2)
          self.do_click(self.FROM)
          time.sleep(2)
          self.do_send_keys(self.FROM_DATA_SEND_KEYS,key1)
          time.sleep(2)
          self.do_click(self.FROM_DATA_CLICK)
          time.sleep(2)
          self.do_send_keys(self.TO_DATA_SEND_KEYS,key2)
          time.sleep(2)
          self.do_click(self.TO_DATA_CLICK)

          time.sleep(4)
          self.do_click(self.DEPARTURE_CLICK)
          time.sleep(4)
          self.do_click(self.DEPARTURE_DATE_CLICK)
          time.sleep(4)
          self.do_click(self.SEARECH_BUTTON_CLICK)

     def get_Count_Of_flights(self):
           return  self.get_Flight_Names_Count(self.FLIGHT_NAMES)

     def get_makemy_Trip_Flight_Names(self):
         self. flights = self.get_elements(self.FLIGHT_NAMES)
         assert  self.flights != [] ,'No flights Found '
         self.starttime =self.get_elements(self.START_TIME)
         assert  self.starttime != [] ,"Starting times are not found "
         self.endtime = self.get_elements(self.END_TIME)
         assert  self.endtime != [], "Ending times are not Found"

         for i, j, k in zip(self. flights, self.starttime, self.endtime):
               data = {"FLIGHT NAME": i.text, "START TIME": j.text, "ARRIVED TIME": k.text}
               print(data)

