from pagesobjets.basecase import BaseCase
from selenium.webdriver.common.by import By
import time
class SendPostPage(BaseCase):
    #快速发帖
    title = (By.ID, "subject")
    content = (By.ID, "fastpostmessage")
    fastpost_button = (By.ID, "fastpostsubmit")
    moren = (By.CSS_SELECTOR, ".fl_icn a")
    iframe = (By.TAG_NAME, "iframe")
    def fastsendfun(self,title1,content1):
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.send_keys(title1,*self.title)
        self.send_keys(content1,*self.content)
        self.click(*self.fastpost_button)
        self.driver.switch_to.window(self.driver.window_handles[0])

    #删除帖子
    title_loc = (By.CSS_SELECTOR, "#threadlisttableid tbody:last-of-type .o")
    delete_loc = (By.CSS_SELECTOR, "#mdly p strong")
    submit_loc = (By.ID, "modsubmit")
    def deletefun(self):
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.click(*self.title_loc)
        self.click(*self.delete_loc)
        self.click(*self.submit_loc)

    #点击发帖
    post_button_loc = (By.ID, "newspecial")
    def click_postfun(self):
        self.click(*self.post_button_loc)

