#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Last modified on 23.06.2012

@author: adrianus
'''

import matplotlib.pyplot as plt

data = [x**2 for x in range(1,20)]

plt.plot(data)
plt.fill()
plt.show()
