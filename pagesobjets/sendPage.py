from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from WebUITest.pagesobjets.basecase import BaseCase
import time
class FaTiePage(BaseCase):

    title = (By.ID, "subject")
    content=(By.ID,"fastpostmessage")
    fatie_button = (By.ID,"fastpostsubmit")
    moren = (By.CSS_SELECTOR,".fl_icn a")
    iframe=(By.TAG_NAME,"iframe")

    def defaultfun(self):
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(5)
        self.driver.implicitly_wait(3)
        self.click(*self.moren)

    def sendfun(self,title1,content1):
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.send_keys(title1,*self.title)
        self.send_keys(content1,*self.content)
        self.click(*self.fatie_button)
        self.driver.switch_to.window(self.driver.window_handles[0])








