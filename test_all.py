import HTMLTestRunner
import os
import unittest
from abs_test import AbsTestCase
from sort_test import SortTestCase

cur_path=os.path.dirname(os.path.realpath(__file__))
report_path=os.path.join(cur_path,"report")
if not os.path.exists(report_path):os.mkdir(report_path)

suite=unittest.TestSuite()
suite.addTest(unittest.makeSuite(AbsTestCase))
suite.addTest(unittest.makeSuite(SortTestCase))

if __name__=="__main__":
    html_report=report_path+r"\result.html"#r定义存放报告的路径
    fp=open(html_report,"wb")
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,verbosity=2,title="单元测试报告",description="用例执行情况")
    runner.run(suite)

