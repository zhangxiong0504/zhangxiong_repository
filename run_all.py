import unittest
from abs_test import AbsTestCase
from sort_test import SortTestCase
suite=unittest.TestSuite()
suite.addTest(unittest.makeSuite(AbsTestCase))
suite.addTest(unittest.makeSuite(SortTestCase))
if __name__=="__main__":
    runner=unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
