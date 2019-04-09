from pagesobjets.basecase import BaseCase
from selenium.webdriver.common.by import By
import time
class StationPage(BaseCase):
    #添加新版块
    manager_loc = (By.PARTIAL_LINK_TEXT, "管理中心")
    # pwd_loc=(By.NAME,"admin_password")
    luntan_loc = (By.ID, "header_forum")
    # submit_loc=(By.NAME,"submit")
    new_loc = (By.CSS_SELECTOR, ".lastboard .addtr")
    iframe_loc = (By.ID, "main")
    submit_editsubmit_loc = (By.ID, "submit_editsubmit")
    def partfun(self):
        # 进入版块管理
        self.click(*self.manager_loc)
        self.driver.switch_to.window(self.driver.window_handles[1])
        # self.send_keys(password,self.pwd_loc)
        # self.click(*self.submit_loc)
        self.click(*self.luntan_loc)
        time.sleep(5)
        # 创建新的版块
        self.find_frame(*self.iframe_loc)
        self.click(*self.new_loc)
        self.click(*self.submit_editsubmit_loc)
        self.driver.switch_to.window(self.driver.window_handles[1])