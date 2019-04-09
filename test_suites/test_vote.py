import unittest
from test_suites.base_testcase import BaseTestCase
from pagesobjets.beforeLoginPage import BeforeLoginPage
from pagesobjets.afterLoginPage import AfterLoginPage
from pagesobjets.voteDetailPage import VoteDetailPage
from pagesobjets.sendVotePage import SendVotePage

import time
class VotePageTest(BaseTestCase):
    def test_vote(self):
        # 用户登录
        beforeLoginPage = BeforeLoginPage(self.driver)
        beforeLoginPage.ordinaryloginfun("guo", "123456")
        self.assertIn("guo", self.driver.page_source, "没有进入登录界面")
        # 发表投票帖子
        # 进行投票
        vote = SendVotePage(self.driver)
        vote.votefun("喜欢运动的程度", "喜欢", "还可以", "不喜欢")
        self.assertIn("您已经投过票", self.driver.page_source, "没有进行投票")
        # 取出投票各个选项的名称以及投票比例
        # 取出投票的主题名称
        time.sleep(5)
        voteDetailPage = VoteDetailPage(self.driver)
        voteDetailPage.voteNamefun()
if __name__ == "__main__":
    unittest.main(verbosity=2)