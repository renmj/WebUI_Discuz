import unittest
import os
import HTMLTestRunner
test_dir="./"
suite=unittest.TestLoader().discover(test_dir,pattern='test_*.py')
#设置报告路径
before_dir=os.path.dirname(os.path.abspath(".")) #当前路径的上一级
print(before_dir)
report_path=os.path.join(before_dir,"test_report") #连接
print(report_path)
if not os.path.exists(report_path):os.mkdir(report_path)
if __name__=="__main__":
    HTML_report = report_path + r"\test_report.html"
    fp = open(HTML_report, "wb")
    htmlrunner = HTMLTestRunner.HTMLTestRunner(stream=fp, verbosity=2, title="单元测试报告", description="测试用例情况")
    htmlrunner.run(suite)

