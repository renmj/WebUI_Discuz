from pagesobjets.basecase import BaseCase
from selenium.webdriver.common.by import By
import time
class BeforeLoginPage(BaseCase):
    admin_name_loc = (By.NAME,"username")
    admin_pwd_loc = (By.NAME,"password")
    admin_login_button_loc = (By.CSS_SELECTOR,"button em")
    #管理员登录
    def adminloginfun(self,name,pwd):
        self.send_keys(name,*self.admin_name_loc)
        self.send_keys(pwd,*self.admin_pwd_loc)
        self.click(*self.admin_login_button_loc)
        self.driver.switch_to.window(self.driver.window_handles[0])


    #普通用户登录
    ordinary_name = (By.NAME, "username")
    ordinary_pwd = (By.NAME, "password")
    ordinary_login_button = (By.CSS_SELECTOR, "button em")
    def ordinaryloginfun(self, name, pwd):
        self.send_keys(name, *self.ordinary_name)
        self.send_keys(pwd, *self.ordinary_pwd)
        self.click(*self.ordinary_login_button)

    #点击新板块
    new_loc = (By.PARTIAL_LINK_TEXT, "新版块名称")
    def newModelfun(self):
        time.sleep(5)
        self.click(*self.new_loc)

    #点击默认版块
    default_loc = (By.PARTIAL_LINK_TEXT, "默认版块")
    def defaultModelfun(self):
        time.sleep(5)
        self.click(*self.default_loc)




