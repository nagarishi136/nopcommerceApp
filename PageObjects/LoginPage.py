import time

from selenium.webdriver.common.by import By


class LoginPage:
    textbox_usename_id="Email"
    textbox_password_id="Password"
    button_login_xpath="//button[@type='submit']"
    link_LogOut_linkText="Logout"

    def __init__(self,driver):
        self.driver=driver
    def setUserName(self,username):
        self.driver.find_element(By.ID, self.textbox_usename_id).clear()

        self.driver.find_element(By.ID,self.textbox_usename_id).send_keys(username)
    def setPassword(self,password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()

        self.driver.find_element(By.ID,self.textbox_password_id).send_keys(password)
    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()
    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT,self.link_LogOut_linkText).click()