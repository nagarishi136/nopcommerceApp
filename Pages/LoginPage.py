import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from Config.config import TestData
from Pages.BasePage import BasePage
from Pages.HomePage import HomePage


class LoginPage(BasePage):
    EMAIL=(By.ID,"email")
    #PASSWORD = (By.CLASS_NAME, "inputtext _55r1 _6luy _9npi")
    PASSWORD=(By.XPATH,'//input[@class="inputtext _55r1 _6luy _9npi"]')
    LOGIN_BUTTON=(By.CLASS_NAME,"_6ltg")

    RATINGS_BUTTON=(By.XPATH, '(//a[text()="Ratings"])[1]')

    def __init__(self,driver):
        super().__init__(driver)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.set_page_load_timeout(50)

    Text = (By.CLASS_NAME, "_9ay7")
    TOTAL_TABLE_ROWS = (By.TAG_NAME, "tr")
    TABLE_DATA = (By.TAG_NAME, "td")
    # TOURNAMENT_BUTTON = (By.XPATH, '//div[@class="container"]/a[3]')
    # COUNTRY_DROP_DOWN = (By.XPATH, '//select[@id="select_country"]')
    TOURNAMENT_BUTTON = (By.CSS_SELECTOR, 'div[class="container"]/a[3]')
    COUNTRY_DROP_DOWN = (By.ID, "select_country")
    COUNTRY_INDIA=(By.XPATH, '//option[text()="India"]')
    Current_And_Future_Periods = (By.ID, "archive")
    #Current_And_Future_Periods = (By.XPATH, '//select[@id="archive"]')
    CURRENT_DATE=(By.XPATH, '//option[@value="2022-02-01"]')
    TABLE_ROWS=(By.XPATH, '//*[@id="main_table"]/tbody/tr')
    TABLE_DATA=(By.XPATH, '//*[@id="main_table"]/tbody/tr[2]/td')
    def get_Login_page_title(self,title):
        return self.get_title()

    def do_invalid_Login(self,username,invalidpassword):
        self.driver.get(TestData.BASE_URL)
        self.do_send_keys(self.EMAIL,username)
        self.do_send_keys(self.PASSWORD,invalidpassword)
        self.do_click(self.LOGIN_BUTTON)

        print("Error Mgs --->",self.get_element_text(self.Text))


        #return HomePage(self.driver)

    def do_valid_Login(self,username,validpassword):
        self.driver.get(TestData.BASE_URL)
        self.do_send_keys(self.EMAIL, username)
        self.do_send_keys(self.PASSWORD,validpassword)
        self.do_click(self.LOGIN_BUTTON)
    def do_fide_task(self):

        self.driver.get(TestData.FIDE_URL)
        self.do_click(self.RATINGS_BUTTON)

    def get_length_rows(self):

        return  self.get_rows_count(self.TOTAL_TABLE_ROWS)
    def get_rows(self):
      return self.get_table_rows(self.TOTAL_TABLE_ROWS)


    def get_length_data(self):
      return  self.get_table_data(self.TABLE_DATA)


    def get_Total_info(self):
        self.info=[]
        self.trs=self.get_web_elements(self.TOTAL_TABLE_ROWS)
        table_data=self.get_web_elements(self.TABLE_DATA)

        self.trs_count=len(self.trs)

        for i in range(self.trs_count):#len(trs)
            self.tds=self.trs[i].self.tds
            self.tds_count = len(self.tds)
            for j in range(self.tds_count):
                if self.tds[j].text == 'IND':
                    self.data = {'Name': self.tds[1].text, 'World Rank': self.tds[0].text, 'Rating': self.tds[3].text, 'B-Day': self.tds[5].text}
                    self.info.append(self.data)
        print(self.info)

    def get_tournaments(self):
        self.do_click(self.TOURNAMENT_BUTTON)
    def click_on_country_drop_down(self):
        self.do_click(self.COUNTRY_DROP_DOWN)

    def enter_text_drop_down(self,text):
        self.do_send_keys(self.COUNTRY_DROP_DOWN,text)

    def select_item(self,option):
        return self.select_by_text(self.COUNTRY_DROP_DOWN,option)
    def select_Current_and_future_periods(self):
        # Click on the tournaments link
        self.do_click(self.TOURNAMENT_BUTTON)
        # Click on the select country drop_down
        self.s = self.get_web_element(self.COUNTRY_DROP_DOWN)
        self.s.click()
        # enter the input on select drop_down filed
        self.s.send_keys('india')
        self.country = Select(self.s)
        # select the value text "IND"
        self.country.select_by_value('IND')
        # Click on the text India
        self.do_click(self.COUNTRY_INDIA)
        # Select on the Current and future periods Drop_Down
        self.dd = self.get_web_element(self.Current_And_Future_Periods)
        self.dd.click()
        time.sleep(2)
        self.match = Select(self.dd)
        # select the current date
        self.match.select_by_value('2022-02-01')
        time.sleep(1)
        # Click on the current date
        self.do_click(self.CURRENT_DATE)
        time.sleep(1)
        print("*" * 50)
        # Total number of Table rows
        self.trs = len(self.get_web_elements(self.TABLE_ROWS))
        # Total number of Table columns
        self.tc = len(self.get_web_elements(self.TABLE_DATA))
        print(self.trs)
        print(self.tc)
        for r in range(2, self.trs + 1):
            for c in range(1, self.tc + 1):
                value = self.driver.find_element(By.XPATH,
                                            '//*[@id="main_table"]/tbody/tr[' + str(r) + ']/td[' + str(c) + ']').text
                print(value)


