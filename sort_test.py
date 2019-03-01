import unittest
from sort import sort
from ddt import ddt,data,unpack


@ddt
class SortTestCase(unittest.TestCase):
    @classmethod
    def setUp(clas):
        print("start sort test")

    @data([0,0,0],[1,0,2],[1,1,10],[1,2,20])
    @unpack

    def test_sort(self,num,type,except_value):
        result=sort(num,type)
        self.assertEqual(result,except_value,msg=result)
    @classmethod
    def tearDown(clas):
        print("end sort test")
if __name__=='__main__':
    unittest.main(verbosity=2)