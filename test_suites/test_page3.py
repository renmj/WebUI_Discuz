import unittest
from WebUITest.test_suites.base_testcase import BaseTestCase
from WebUITest.pagesobjets.findContentPage import FindContentPage
from selenium.webdriver.common.by import By
from WebUITest.pagesobjets.exitPage import ExitPage
import time

class PageTestThree(BaseTestCase):


    def test_pageTestThree(self):
        # 用户登录
        # 进行帖子搜索
        # 搜索haotest帖子
        # 进入搜索的帖子
        # 验证帖子标题和期望的一致
        findCotent=FindContentPage(self.driver)
        findCotent.findContentfun("haotest")
        self.driver.switch_to.window(self.driver.window_handles[2])
        self.assertIn("haotest", self.driver.title,"标题中没有haotest")
        #用户退出
        exit = ExitPage(self.driver)
        exit.exitfun()
        time.sleep(5)
        self.assertIn("登录", self.driver.page_source,"没有退出成功")


if __name__ == "__main__":
    unittest.main(verbosity=2)