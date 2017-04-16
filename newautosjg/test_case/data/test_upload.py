#!/usr/bin/env python
# coding=utf-8
from autosjg.index import Login
from autosjg.test_case.com import switch

class Testupload(Login):

    def test_01app(self):
        pass

    def test_02file(self):
        switch.data(self.driver)
        print self.driver.title

    def test_03database(self):
        pass

    def test_04joindata(self):
        pass

    def test_05connectdata(self):
        pass

    def test_06etl(self):
        pass

