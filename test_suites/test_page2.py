import unittest
from WebUITest.test_suites.base_testcase import BaseTestCase
from WebUITest.pagesobjets.loginAdminPage import LoginAdmin
from WebUITest.pagesobjets.sendPage import FaTiePage
from WebUITest.pagesobjets.deletePage import DeletePage
from WebUITest.pagesobjets.partPage import PartPage
from WebUITest.pagesobjets.loginPage import LoginPage
from WebUITest.pagesobjets.newModelPage import NewModel
class PageTestTwo(BaseTestCase):
    def test_pageTestTwo(self):
        #管理员登录
        loginadmin=LoginAdmin(self.driver)
        loginadmin.loginPagefun("admin","guo123")
        self.assertIn("admin", self.driver.page_source, "没有进入登录界面")
        #进入默认板块
        morenPage=FaTiePage(self.driver)
        morenPage.defaultfun()
        self.assertIn("默认版块", self.driver.title, "没有进入默认板块")
        #删除帖子
        deletePage=DeletePage(self.driver)
        deletePage.deletefun()

        # 创建新的版块
        partPage=PartPage(self.driver)
        partPage.partfun()

        #普通用户登录
        login = LoginPage(self.driver)
        login.loginfun("guo", "123456")
        self.assertIn("guo", self.driver.page_source, "没有进入登录界面")
        #在新的版块下发帖回帖
        newModel=NewModel(self.driver)
        newModel.newModelfun()



if __name__=="__main__":
    unittest.main(verbosity=2)




