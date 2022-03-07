from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC


"""" This Class is the Parent of all Pages  """
""" It contains all the generic methods and utilities for all the pages """
class BasePage:
      def __init__(self,driver):
          self.driver=driver
          self.wait=WebDriverWait(self.driver,10)


      def do_click(self,by_Locator):
          WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_Locator)).click()

      def do_send_keys(self, by_Locator,text):
          WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_Locator)).send_keys(text)

      def get_element_text(self, by_Locator):
          return self.wait.until(EC.presence_of_element_located(by_Locator)).text

      def is_enabled(self, by_Locator):
          element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_Locator))
          return bool(element)

      def get_title(self, title):
          WebDriverWait(self.driver, 10).until(EC.title_is(title))
          return self.driver.title
      def get_count(self,by_Locator):
         return  len(self.wait.until(EC.presence_of_all_elements_located(by_Locator)))


      def get_web_elements(self,by_Locator):
          return self.wait.until(EC.presence_of_all_elements_located(by_Locator))

      def get_web_element(self,by_Locator):
          return  self.wait.until(EC.presence_of_element_located(by_Locator))
      def get_table_rows(self,by_Locator):
          return WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(by_Locator))

      def get_elements(self,by_Locator):
          return self.wait.until(EC.presence_of_all_elements_located(by_Locator))


      def select_by_text(self,by_Locator,option):
          select=Select(self.get_element(by_Locator))
          select.select_by_visible_text(option)
      def get_Flight_Names_Count(self,by_Locator):
          return len(WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(by_Locator)))

