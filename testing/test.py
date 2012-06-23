#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Last modified on 04.05.2012

@author: adrianus
'''

import unittest
import Bookshelf

class Test(unittest.TestCase):

    def setUp(self):
        self.b = Bookshelf.Bookshelf()
        self.b.add("Testbuch")
    
    def testSize(self):
        self.failIf(self.b.length() != 1)
    
    def testName(self):
        self.failUnless(self.b.first_book()[:4] == "Test")
        
    def testType(self):
        self.failUnless(str(type(self.b)) == "<class 'Bookshelf.Bookshelf'>")
    
if __name__ == "__main__":
    unittest.main()
