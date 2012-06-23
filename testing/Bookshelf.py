#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Last modified on 04.05.2012

@author: adrianus
'''

class Bookshelf(object):
    '''
    Represents a simple bookshelf.
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
        self.data = []

    def add(self, x):
        self.data.append(x)
        
    def info(self):
        print(str(len(self.data)) + " books registered at the moment.")
        
    def length(self):
        return len(self.data)
    
    def first_book(self):
        return self.data[0]
