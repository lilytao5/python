# coding=utf-8
import unittest

class Baibu(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_01(self):
        u"""测试百度---搜索1"""
        a = 1
        self.assertEqual(a,2)
    def test_02(self):
        u"""测试百度---搜索2"""
        b = 2
        self.assertEqual(b,2)

    def test_03(self):
        u"""测试百度---搜索3"""
        c = 3
        self.assertEqual(c,3)

class Google(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_01(self):
        a = 1
        self.assertEqual(a,1)
    def test_02(self):
        b = 2
        self.assertEqual(b,2)

    def test_03(self):
        c = 3
        self.assertEqual(c,3)

if __name__=='__main__':
    unittest.main()
