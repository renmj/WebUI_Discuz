import unittest
from test_suites.base_testcase import BaseTestCase
from pagesobjets.beforeLoginPage import BeforeLoginPage
from pagesobjets.afterLoginPage import AfterLoginPage

import time
class SearchPostTest(BaseTestCase):
    def test_search(self):
        # 普通用户登录
        beforelogin = BeforeLoginPage(self.driver)
        beforelogin.ordinaryloginfun("guo", "123456")
        self.assertIn("guo", self.driver.page_source, "没有进入登录界面")
        # 进行帖子搜索
        # 搜索haotest帖子
        # 进入搜索的帖子
        # 验证帖子标题和期望的一致
        afterLoginPage = AfterLoginPage(self.driver)
        afterLoginPage.findContentfun("haotest")
        self.driver.switch_to.window(self.driver.window_handles[2])
        self.assertIn("haotest", self.driver.title, "标题中没有haotest")
        # 用户退出
        afterLoginPage.exitfun()
        time.sleep(5)


if __name__ == "__main__":
    unittest.main(verbosity=2)