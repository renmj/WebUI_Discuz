import unittest
from test_suites.base_testcase import BaseTestCase
from pagesobjets.beforeLoginPage import BeforeLoginPage
from pagesobjets.afterLoginPage import AfterLoginPage
from pagesobjets.stationPage import StationPage
from pagesobjets.sendPostPage import SendPostPage
import time
class NewModelPageTest(BaseTestCase):
    def test_newModelfun(self):
        # 管理员登录
        beforeLoginPage =BeforeLoginPage(self.driver)
        beforeLoginPage.adminloginfun("admin", "guo123")
        self.assertIn("admin", self.driver.page_source, "没有进入登录界面")
        # 点击进入默认板块
        beforeLoginPage.defaultModelfun()
        self.assertIn("默认版块", self.driver.title, "没有进入默认板块")
        # 删除帖子
        sendPostPage = SendPostPage(self.driver)
        sendPostPage.deletefun()

        #点击管理中心
        afterLoginPage=AfterLoginPage(self.driver)
        afterLoginPage.clickManager()
        # 创建新的版块
        stationPage = StationPage(self.driver)
        stationPage.partfun()
        #退出
        afterLoginPage.exitfun()
        afterLoginPage.exitfun()

        # 普通用户登录
        beforeLoginPage = BeforeLoginPage(self.driver)
        beforeLoginPage.ordinaryloginfun("guo", "123456")
        self.assertIn("guo", self.driver.page_source, "没有进入登录界面")
        # 在新的版块下发帖回帖
        sendPostPage.fastsendfun("titlettttttt","contenttttttttttttttttttttt")
if __name__=="__main__":
    unittest.main(verbosity=2)