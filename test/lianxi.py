# coding=utf-8
import unittest

class Lx(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_1(self):
        a = 1
        self.assertEqual(a,1)
    def test_2(self):
        b = 2
        self.assertEqual(b,2)

if __name__=='__main__':
    unittest.main()
