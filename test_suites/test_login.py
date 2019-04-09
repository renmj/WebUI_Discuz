import unittest
from test_suites.base_testcase import BaseTestCase
from pagesobjets.beforeLoginPage import BeforeLoginPage
from pagesobjets.afterLoginPage import AfterLoginPage
from pagesobjets.replySendPage import ReplySendPage
from pagesobjets.sendPostPage import SendPostPage

import time
class LoginPageTest(BaseTestCase):

    def test_login(self):
        #普通用户登录
        beforelogin= BeforeLoginPage(self.driver)
        beforelogin.ordinaryloginfun("guo","123456")
        self.assertIn("guo", self.driver.page_source, "没有进入登录界面")
        #点击默认板块
        afterLogin=AfterLoginPage(self.driver)
        afterLogin.defaultModelfun()
        self.assertIn("默认版块", self.driver.title,"没有进入默认板块")
        #快速发帖
        sendPage=SendPostPage(self.driver)
        sendPage.fastsendfun("titlettttttt","contenttttttttttttttttttttt")
        self.assertIn("发表于", self.driver.page_source,"没有发表成功")
        #默认板块回帖
        replySendPage=ReplySendPage(self.driver)
        replySendPage.replyfun("hellovvvvvvvvvvvvvvvvvvvv")
        self.assertIn("发表回复", self.driver.page_source, "没有回复成功")
        #退出
        afterLogin.exitfun()

if __name__=="__main__":
    unittest.main(verbosity=2)


