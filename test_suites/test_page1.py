import unittest
from WebUITest.test_suites.base_testcase import BaseTestCase
from ddt import ddt,unpack,data
from WebUITest.pagesobjets.loginPage import LoginPage
from WebUITest.pagesobjets.replyPage import ReplyPage
from WebUITest.pagesobjets.sendPage import FaTiePage
from WebUITest.pagesobjets.exitPage import ExitPage
from WebUITest.pagesobjets.replyPage import ReplyPage
import time
class PageTestOne(BaseTestCase):

    def test_login(self):
        #普通用户登录
        login= LoginPage(self.driver)
        login.loginfun("guo","123456")
        self.assertIn("guo", self.driver.page_source, "没有进入登录界面")
        #默认板块发帖
        fatiePage=FaTiePage(self.driver)
        fatiePage.defaultfun()
        self.assertIn("默认版块", self.driver.title,"没有进入默认板块")
        fatiePage.sendfun("titlettttttt","contenttttttttttttttttttttt")
        self.assertIn("发表于", self.driver.page_source,"没有发表成功")
        #默认板块回帖
        replyPage=ReplyPage(self.driver)
        replyPage.replyfun("hellovvvvvvvvvvvvvvvvvvvv")
        self.assertIn("发表回复", self.driver.page_source, "没有回复成功")
        #退出
        exitpage=ExitPage(self.driver)
        exitpage.exitfun()
        self.assertIn("登录", self.driver.page_source, "没有退出成功")



if __name__=="__main__":
    unittest.main(verbosity=2)


