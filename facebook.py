from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import itertools

s = Service(r"C:\Users\Nagamalla Reddy-2639\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.implicitly_wait(10)
driver.get("https://www.facebook.com/")
driver.maximize_window()
driver.find_element(By.ID,"email").send_keys('reddyrishi136@gmail.com')
driver.find_element(By.XPATH,'//input[@class="inputtext _55r1 _6luy _9npi"]').send_keys("1234567")
driver.find_element(By.CLASS_NAME,"_6ltg").click()
print(driver.find_element(By.XPATH,"//div[@class='_9ay7']").text)
driver.close()
