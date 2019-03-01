from WebUITest.test_suites.base_testcase import BaseTestCase
from WebUITest.pagesobjets.voteNamePage import VoteNamePage
from WebUITest.pagesobjets.votePage import VotePage
from WebUITest.pagesobjets.loginPage import LoginPage
import time
class PageTestFour(BaseTestCase):
    def test_vote(self):
        #用户登录
        login = LoginPage(self.driver)
        login.loginfun("guo","123456")
        self.assertIn("guo", self.driver.page_source, "没有进入登录界面")
        # 发表投票帖子
        # 进行投票
        vote=VotePage(self.driver)
        vote.votefun("喜欢运动的程度","喜欢","还可以","不喜欢")
        self.assertIn("您已经投过票", self.driver.page_source, "没有进行投票")
        # 取出投票各个选项的名称以及投票比例
        # 取出投票的主题名称
        time.sleep(5)
        votename=VoteNamePage(self.driver)
        votename.voteNamefun()




