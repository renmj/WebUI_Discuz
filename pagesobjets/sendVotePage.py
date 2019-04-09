from pagesobjets.basecase import BaseCase
from selenium.webdriver.common.by import By
from pagesobjets.sendPostPage import SendPostPage
from pagesobjets.beforeLoginPage import BeforeLoginPage
import time
class SendVotePage(BaseCase):

    vote_loc=(By.LINK_TEXT,"发起投票")
    title_loc=(By.ID,"subject")
    content1_loc=(By.XPATH,"//div[@id='pollm_c_1']/p[1]/input")
    content2_loc = (By.XPATH, "//div[@id='pollm_c_1']/p[2]/input")
    content3_loc = (By.XPATH, "//div[@id='pollm_c_1']/p[3]/input")
    iframe_loc=(By.ID,"e_iframe")
    content_body_loc=(By.TAG_NAME,"body")
    send_loc=(By.NAME,"topicsubmit")
    option_loc=(By.CLASS_NAME,"pslt")
    submit_loc=(By.ID,"pollsubmit")
    def votefun(self,title,con1,con2,con3):
        #点击进入默认板块
        beforeLoginPage=BeforeLoginPage(self.driver)
        beforeLoginPage.defaultModelfun()
        self.driver.switch_to.window(self.driver.window_handles[0])
        #点击发帖
        sendPostPage=SendPostPage(self.driver)
        sendPostPage.click_postfun()
        #点击发起投票
        self.click(*self.vote_loc)
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.send_keys(title,*self.title_loc)
        self.send_keys(con1,*self.content1_loc)
        self.send_keys(con2, *self.content2_loc)
        self.send_keys(con3, *self.content3_loc)
        self.click(*self.send_loc)
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.click(*self.option_loc)
        self.click(*self.submit_loc)





