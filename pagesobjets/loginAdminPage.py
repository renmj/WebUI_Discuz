from WebUITest.pagesobjets.basecase import BaseCase
from selenium.webdriver.common.by import By
import time
class LoginAdmin(BaseCase):
    name = (By.NAME,"username")
    pwd = (By.NAME,"password")
    login_button = (By.CSS_SELECTOR,"button em")

    def loginPagefun(self,name,pwd):

        self.send_keys(name,*self.name)
        self.send_keys(pwd,*self.pwd)
        self.click(*self.login_button)
        self.driver.switch_to.window(self.driver.window_handles[0])