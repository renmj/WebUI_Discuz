from pagesobjets.basecase import BaseCase
from selenium.webdriver.common.by import By
from pagesobjets.beforeLoginPage import BeforeLoginPage
import time
class AfterLoginPage(BaseCase):
    # 点击新板块
    new_loc = (By.PARTIAL_LINK_TEXT, "新版块名称")
    def newModelfun(self):
        time.sleep(5)
        self.click(*self.new_loc)


    # 点击默认版块
    default_loc = (By.PARTIAL_LINK_TEXT, "默认版块")
    def defaultModelfun(self):
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(5)
        self.driver.implicitly_wait(3)
        self.click(*self.default_loc)

    # 点击管理中心
    manager_loc = (By.PARTIAL_LINK_TEXT, "管理中心")
    def clickManager(self):
        self.click(*self.manager_loc)
        self.driver.switch_to.window(self.driver.window_handles[1])

    #点击退出
    exit = (By.LINK_TEXT, "退出")
    def exitfun(self):
        self.click(*self.exit)

    #搜索帖子
    find_loc = (By.ID, "scbar_txt")
    find_button_loc = (By.ID, "scbar_btn")
    find_hotest_loc = (By.CSS_SELECTOR, ".xs3 font")

    def findContentfun(self, content):
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.send_keys(content, *self.find_loc)
        self.click(*self.find_button_loc)
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.click(*self.find_hotest_loc)
        time.sleep(5)