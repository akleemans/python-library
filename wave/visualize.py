#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Last modified on 23.06.2012

@author: adrianus
'''

import matplotlib.pyplot as plt
import wave, struct

waveFile = wave.open('10sec.wav', 'r')
data = list()

for i in range(0, waveFile.getnframes()):
    d = struct.unpack("<h", waveFile.readframes(1))
    data.append(int(d[0]))

plt.plot(data)
plt.fill()
plt.show()
