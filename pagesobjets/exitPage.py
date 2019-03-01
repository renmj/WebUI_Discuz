from WebUITest.pagesobjets.basecase import BaseCase
from selenium.webdriver.common.by import By
class ExitPage(BaseCase):

    exit = (By.LINK_TEXT,"退出")
    def exitfun(self):
        self.click(*self.exit)