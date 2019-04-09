from pagesobjets.basecase import BaseCase
from selenium.webdriver.common.by import By
import time
class ReplySendPage(BaseCase):
    reply = (By.ID, "post_replytmp")
    reply_content = (By.CSS_SELECTOR, "div textarea")
    re_button = (By.ID, "postsubmit")
    moren = (By.CSS_SELECTOR, ".fl_icn a")

    def replyfun(self, content):
        self.click(*self.reply)
        # self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(5)
        self.send_keys(content, *self.reply_content)
        self.click(*self.re_button)