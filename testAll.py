import os
import sys
import unittest
import HTMLTestRunner
from test_suites.test_login import LoginPageTest
from test_suites.test_searchpost import SearchPostTest
from test_suites.test_vote import VotePageTest
from test_suites.test_newmodelpost import NewModelPageTest
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
sys.path.append("E:\\pythonWorkplace\\UITest\\WebUITest")
current_path = os.path.abspath(__file__)
a_path= os.path.dirname(current_path)
test_dir =a_path +'/test_suites/'
print(test_dir)
suite=unittest.TestLoader().discover(test_dir,pattern='test_*.py') #第一个参数测试文件的路径，第二个匹配文件
#构建测试套件
# suite=unittest.TestSuite()
# suite.addTest(unittest.makeSuite(LoginPageTest))
# suite.addTest(unittest.makeSuite(SearchPostTest))
# suite.addTest(unittest.makeSuite(VotePageTest))
# suite.addTest(unittest.makeSuite(NewModelPageTest))
#设置报告路径


report_path =a_path+'/reporter/'
print(report_path)
if not os.path.exists(report_path):os.mkdir(report_path)
if __name__=="__main__":
    HTML_report = report_path + r"\test_report.html"
    fp = open(HTML_report, "wb")
    htmlrunner = HTMLTestRunner.HTMLTestRunner(stream=fp, verbosity=2, title="单元测试报告", description="测试用例情况")
    htmlrunner.run(suite)

