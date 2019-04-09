from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework.logger import Logger
from selenium.webdriver.common.by import By
import os
import time
logger=Logger(logger="BaseCase").getlog()
class BaseCase(object):
    def __init__(self,driver):
        self.driver=driver

    def back(self):
        self.driver.back()
        logger.info("back")
    def forward(self):
        self.driver.forward()
        logger.info("forward")
    def get_url(self,url):
        self.driver.get(url)
        logger.info("get_url")
    def quit(self):
        self.driver.quit()
        logger.info("quit")
    def close(self):
        try:
            self.driver.close()
            logger.info("close this window")
        except Exception as e:
            logger.error("failed to close this window")
    def find_element(self,*loc):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
            logger.info("find_elemen",loc)
        except:
            logger.error("%s page not found element%s元素"% (self,loc))
    def find_frame(self,*loc):
        el=self.find_element(*loc)
        self.driver.switch_to.frame(el)
        logger.info("into frame")
    def get_windows_img(self):
        file_path=os.path.dirname(os.path.abspath("."))+'/screenshorts/'
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("get_windows_img")
        except:
            self.get_windows_img()
            logger.error("not get_windows_img")

    def get_text(self,*loc):
        try:
            el = self.find_element(*loc)
            print(el.text)
            logger.info("内容为"+el.text)
        except:
            logger.error("没有找到")


    def send_keys(self,text,*loc):
        ele_content=self.find_element(*loc)
        # ele_content.clear()
        try:
            ele_content.send_keys(text)
            logger.info("send_keys"+text)
        except:
            logger.error("not send_keys")
    def click(self,*loc):
        try:
            ele_button=self.driver.find_element(*loc)
            ele_button.click()
            logger.info("click")
        except:
            logger.error("not click")
    def clear(self,*loc):
        try:
            ele=self.driver.find_element(*loc)
            ele.clear()
            logger.info("clear")
        except:
            logger.error("not clear")





