from WebUITest.pagesobjets.basecase import BaseCase
from selenium.webdriver.common.by import By
from WebUITest.pagesobjets.loginPage import LoginPage
from WebUITest.pagesobjets.replyPage import ReplyPage
import time
class FindContentPage(BaseCase):
    find_loc=(By.ID,"scbar_txt")
    find_button_loc=(By.ID,"scbar_btn")
    find_hotest_loc=(By.CSS_SELECTOR,".xs3 font")



    def findContentfun(self,content):
        login = LoginPage(self.driver)
        login.loginfun("guo","123456")
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.send_keys(content,*self.find_loc)
        self.click(*self.find_button_loc)
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.click(*self.find_hotest_loc)
        time.sleep(5)



