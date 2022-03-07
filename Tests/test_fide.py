from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

class Test_Fide:

    def test_Login_Page(self):
            global driver
            s = Service(r"C:\Users\Nagamalla Reddy-2639\drivers\chromedriver.exe")
            driver = webdriver.Chrome(service=s)
            driver.maximize_window()
            driver.implicitly_wait(5)
            driver.set_page_load_timeout(50)
            # Open the FIDE website
            driver.get('https://www.fide.com/')

    def test_list_Out_Indian_Players_Page(self):
        driver.find_element(By.XPATH, '(//a[text()="Ratings"])[1]').click()
        trs = driver.find_elements(By.TAG_NAME, "tr")

        print("Total number of rows: ")
        print(len(trs))

        info = []
        for i in range(len(trs)):
            tds = trs[i].find_elements(By.TAG_NAME, "td")
            for j in range(len(tds)):
                if tds[j].text == 'IND':
                    data = {'Name': tds[1].text, 'World Rank': tds[0].text, 'Rating': tds[3].text, 'B-Day': tds[5].text}
                    info.append(data)

        print(info)
    def test_list_out_the_current_tournaments_page(self):
            driver.find_element(By.XPATH, '//div[@class="container"]/a[3]').click()
            # Click on the select country drop_down
            s = driver.find_element(By.XPATH, '//select[@id="select_country"]')
            s.click()
            # enter the input on select drop_down filed
            s.send_keys('india')
            country = Select(s)
            # select the value text "IND"
            country.select_by_value('IND')
            # Click on the text India
            driver.find_element(By.XPATH, '//option[text()="India"]').click()
            # Select on the Current and future periods Drop_Down
            dd = driver.find_element(By.XPATH, '//select[@id="archive"]')
            dd.click()
            time.sleep(2)
            match = Select(dd)
            # select the current date
            match.select_by_value('2022-02-01')
            time.sleep(1)
            # Click on the current date
            driver.find_element(By.XPATH, '//option[@value="2022-02-01"]').click()
            time.sleep(1)
            print("*" * 50)
            # Total number of Table rows
            trs = len(driver.find_elements(By.XPATH, '//*[@id="main_table"]/tbody/tr'))
            # Total number of Table columns
            tc = len(driver.find_elements(By.XPATH, '//*[@id="main_table"]/tbody/tr[2]/td'))
            # print(trs)
            # print(tc)
            for r in range(2, trs + 1):
                for c in range(1, tc + 1):
                    value = driver.find_element(By.XPATH,
                                                '//*[@id="main_table"]/tbody/tr[' + str(r) + ']/td[' + str(c) + ']').text
                    print(value)


    def test_LogOut_Page(self):
        time.sleep(5)
        driver.quit()