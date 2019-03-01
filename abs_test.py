import unittest
from abs import abs
from ddt import ddt,data,unpack
@ddt
class AbsTestCase(unittest.TestCase):

    def setUp(self):
        print("start abs test")

    @data([1,1],[-1,1],[0,0])
    @unpack

    def test_abs(self,n,except_value):
        result=abs(n)
        self.assertEqual(result,except_value,msg=result)

    def tearDown(self):
        print("end abs test")

if __name__=='__main__':
    unittest.main(verbosity=2)