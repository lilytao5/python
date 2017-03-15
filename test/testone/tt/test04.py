# coding:utf-8
import test01

class Test(test01.TestCase):
    def setUp(self):
        print "0000"

    def tearDown(self):
        print "end"

    def test01(self):
        a = 1
        print "1111111111"
        self.assertEqual(a,1)

    def test02(self):
        b =2
        print "222222"
        self.assertEqual(b,2)
