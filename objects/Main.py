# -*- coding: UTF-8 -*-
'''
Created on 03.05.2012

@author: adrianus
'''

import time
import numpy as np
import matplotlib.pyplot as plt

import Bookshelf

if __name__ == '__main__':

    # some test loop
    for i in range(10):
        if i%3 == 0:
            print("lulz! " + str(i) + " is dividable by 3!")
        else:
            print "i has the value", i
    
    # some test drawing
    x = np.arange(0, 10, 0.1)
    y = np.cos(x)
    
    plt.plot(x, y)
    plt.grid(True)
    #plt.show() #avoid showing the drawing each time
    
    # some sorting in numpy, with timing
    t1 = time.time()
    l = list()
    l = np.random.random_integers(1, 10000000, 1000000)
    l.sort()
    t2 = time.time()
    
    print("Calculation took " + str(t2-t1) + " seconds")
    print("Smallest number: " + str(min(l)) + ", biggest number: " + str(max(l)))
    
    # some test objects
    b = Bookshelf.Bookshelf()
    b.add("Der Schimmelreiter")
    b.add("The Hunger Games")
    b.add("A Study in Scarlet")
    b.info()
    