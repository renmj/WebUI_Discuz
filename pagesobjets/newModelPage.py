from WebUITest.pagesobjets.basecase import BaseCase
from selenium.webdriver.common.by import By
from WebUITest.pagesobjets.sendPage import FaTiePage
from WebUITest.pagesobjets.replyPage import ReplyPage

import time

class NewModel(BaseCase):
    new_loc=(By.PARTIAL_LINK_TEXT,"新版块名称")

    def newModelfun(self):
        time.sleep(5)
        self.click(*self.new_loc)
        fatie = FaTiePage(self.driver)
        fatie.fatiefun("title.....","hhhhhhhhhfffffffffffffffffffff")
        replyPage=ReplyPage(self.driver)
        replyPage.replyfun("fdsjaflsjfl")




