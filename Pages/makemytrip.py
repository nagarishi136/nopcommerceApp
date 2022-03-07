from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import NoSuchElementException




s = Service(r"C:\Users\Nagamalla Reddy-2639\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.implicitly_wait(5)

# Open the makemytrip website
driver.get('https://www.makemytrip.com/flights/')
time.sleep(3)

# click on the From text filed
element=driver.find_element(By.XPATH, "//div[@class='fsw_inputBox searchCity inactiveWidget ']//label")
driver.execute_script("arguments[0].click();", element)
time.sleep(5)
#enter the input in from filed
driver.find_element(By.XPATH, "//div[@class='hsw_autocomplePopup autoSuggestPlugin ']//div//input").send_keys("mumb")
time.sleep(5)

#1.*************************************************************************************************************************
#select the from place

places = driver.find_elements(By.XPATH, "//p[@class='font14 appendBottom5 blackText']")

for place in places:
    print(place.text)
    if place.text == "Mumbai, India":
        place.click()
        break
time.sleep(3)
#2.*****************************************************************************************************************************

#Select The To place
driver.find_element(By.XPATH, "//div[@class='hsw_autocomplePopup autoSuggestPlugin makeFlex column spaceBetween']//div//input").send_keys("del")
time.sleep(4)
to_Places = driver.find_elements(By.XPATH, "//p[@class='font14 appendBottom5 blackText']")
#StaleElementReferenceException
try:
    for to_Place in to_Places:
        print(to_Place.text)
        if to_Place.text == "New Delhi, India":
            time.sleep(2)
            driver.execute_script("arguments[0].click();", to_Place)
            break
    time.sleep(3)
except StaleElementReferenceException as st :
      raise st
#3.***************************************************************************************************************************
#SELECT FROM DATE

from_date=driver.find_elements(By.XPATH,"(//div[@class='DayPicker-Body'])[1]//div[@class='DayPicker-Week']//div[contains(@aria-disabled,'false')]")

for ele in from_date:
    if ele.text == "28":
        ele.click()

time.sleep(3)
#NoSuchElementException
try:
    return_date=driver.find_element(By.XPATH,"//div[@class='fsw_inputBox dates reDates inactiveWidget ']//div[@data-cy='returnArea']//label")
    action=ActionChains(driver)
    action.double_click(return_date).perform()

except NoSuchElementException as nse:
    raise nse
time.sleep(3)
#4.****************************************************************************************************************************
#4.SELECT TO DATE

to_Dates=driver.find_elements(By.XPATH,"(//div[@class='DayPicker-Body'])[2]//div[@class='DayPicker-Week']//div[contains(@aria-disabled,'false')]")
try:
    for to_Date in to_Dates:
        print(to_Date.text)
        if to_Date.text == "3":
            time.sleep(2)
            driver.execute_script("arguments[0].click();", to_Date)
            break
    time.sleep(5)
except StaleElementReferenceException as st:
       raise st
#***********************************************************************************************************************
#5.CLICK ON THE SEARCH BUTTON
try:
  search=driver.find_element(By.XPATH,"//p[@data-cy='submit']//a")
  driver.execute_script("arguments[0].click();", search)

except StaleElementReferenceException as ser:
    raise ser
    time.sleep(6)

try:
    ele1=driver.find_element(By.XPATH, '//*[@id="flightCard-5000"]/div/button')
    driver.execute_script("arguments[0].click();", ele1)
    time.sleep(2)
    driver.execute_script("window.scrollBy(0,8000)", "")
    ele2=driver.find_element(By.XPATH, '//*[@id="flightCard-5001"]/div/button')
    driver.execute_script("arguments[0].click();", ele2)
    time.sleep(2)
except ElementNotInteractableException as en:
       raise en
# try:
#     driver.execute_script("window.scrollBy(0,3100)", "")
#     ele3=driver.find_element(By.XPATH,'//*[@id="flightCard-5002"]/div/button')
#     driver.execute_script("arguments[0].click();", ele3)
#     time.sleep(5)
#
# except NoSuchElementException as ns:
#        raise ns
time.sleep(2)
#***********************************************************************************************************************

flight_Names=driver.find_elements(By.XPATH, "//div[@class='paneView'][1]//span[@class='boldFont blackText']")
flight_Starting_Times=driver.find_elements(By.XPATH,"//div[@class='paneView'][1]//div[contains(@class,'Left')]//p[contains(@class,'blackText')]")
flight_Ending_Times=driver.find_elements(By.XPATH,"//div[@class='paneView'][1]//div[contains(@class,'Right')]//p[contains(@class,'blackText')]")
print(len(flight_Names))
for i,j,k in zip(flight_Names,flight_Starting_Times,flight_Ending_Times):
    data={"FLIGHT NAME":i.text,"START TIME":j.text,"ARRIVED TIME":k.text}
    print(data)
#driver.quit()










