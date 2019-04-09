from pagesobjets.basecase import BaseCase
from selenium.webdriver.common.by import By
from pagesobjets.sendVotePage import SendVotePage
class VoteDetailPage(BaseCase):
    name1_loc=(By.XPATH,"//*[@class='pcht']/table/tbody/tr[1]")
    pensent1_loc=(By.XPATH,"//*[@class='pcht']/table/tbody/tr[2]")
    name2_loc = (By.XPATH, "//*[@class='pcht']/table/tbody/tr[3]")
    pensent2_loc = (By.XPATH, "//*[@class='pcht']/table/tbody/tr[4]")
    name3_loc = (By.XPATH, "//*[@class='pcht']/table/tbody/tr[5]")
    pensent3_loc = (By.XPATH, "//*[@class='pcht']/table/tbody/tr[6]")
    title_loc=(By.ID,"thread_subject")
    def voteNamefun(self):
        votePage=SendVotePage(self.driver)
        print("名称：")
        votePage.get_text(*self.name1_loc)
        votePage.get_text(*self.pensent1_loc)
        votePage.get_text(*self.name2_loc)
        votePage.get_text(*self.pensent2_loc)
        votePage.get_text(*self.name3_loc)
        votePage.get_text(*self.pensent3_loc)
        print("主题：")
        votePage.get_text(*self.title_loc)





