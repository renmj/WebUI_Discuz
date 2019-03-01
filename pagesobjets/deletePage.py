from WebUITest.pagesobjets.basecase import BaseCase
from selenium.webdriver.common.by import By
from WebUITest.pagesobjets.partPage import PartPage
class DeletePage(BaseCase):
    title_loc=(By.CSS_SELECTOR,"#threadlisttableid tbody:last-of-type .o")
    delete_loc=(By.CSS_SELECTOR,"#mdly p strong")
    submit_loc=(By.ID,"modsubmit")

    def deletefun(self):

        self.driver.switch_to.window(self.driver.window_handles[0])
        self.click(*self.title_loc)
        self.click(*self.delete_loc)
        self.click(*self.submit_loc)