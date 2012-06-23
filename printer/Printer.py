#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Last modified on 23.06.2012

@author: adrianus
'''

s = "lulz"

print "Printing..."
lp = open("/dev/lp0", "w")
lp.write(s)
