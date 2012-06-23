#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Last modified on 15.05.2012

@author: adrianus
'''

import Sort
import random
import time

def checkSorted(a):
	for i in xrange(1, len(a) - 1):
		if a[i] < a[i-1]:
			return False
	return True

def main():
	# sample data
	n = 10000
	lst = list()
	
	# generate random array
	for i in xrange(n):
		lst.append(random.randint(1, n*10))
		# lst = np.random.random_integers(1, 10000000, 1000000) 
	
	# sort()
	lstcopy = list(lst)
	t1 = time.time() 
	lstcopy.sort() 
	t2 = time.time()
	print("Calculation of python sort() took " + str(t2-t1) + " seconds")
	
	# mergesort
	lstcopy = list(lst)
	t1 = time.time() 
	lstcopy = Sort.mergesort(lst)
	t2 = time.time()
	print("Calculation of Sort.mergesort() took " + str(t2-t1) + " seconds")

	# quicksort
	lstcopy = list(lst)
	t1 = time.time() 
	lstcopy = Sort.quicksort(lst)
	t2 = time.time()
	print("Calculation of Sort.quicksort() took " + str(t2-t1) + " seconds")

if __name__ == "__main__":
    main()
