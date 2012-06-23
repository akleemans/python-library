#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Last modified on 14.05.2012

@author: adrianus
'''

import time  
import numpy as np

if __name__ == "__main__": 
	print("Sorting 1 million integers, ranging from 1 to 10 million.") 
	t1 = time.time() 
	l = list()
	l = np.random.random_integers(1, 10000000, 1000000) 
	l.sort() 
	t2 = time.time()
	print("Calculation took " + str(t2-t1) + " seconds")
	print("Smallest n: " + str(min(l)) + ", biggest n: " + str(max(l)))
