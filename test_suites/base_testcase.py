from selenium import webdriver
import unittest
from framework.browser_engine import BrowserEngin
import os
import time
class BaseTestCase(unittest.TestCase):
    def setUp(self):
        browser = BrowserEngin()
        self.driver=browser.open_browser()
        print("start")
    def tearDown(self):
        self.driver.quit()
        print("end")





