#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Last modified on 23.06.2012

@author: adrianus
'''

binary = """
01001000
01100101
01101100
01101100
01101111
00100000
01010111
01101111
01110010
01101100
01100100
00100001
00100000
"""

binary = binary.split()
print 'binary code:', binary
plain = ''

for char in binary:
	plain += chr(int(char, 2))

print 'Plain text:', plain
