#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Last modified on 28.06.2012

@author: adrianus
'''

f = open('text.txt', 'r')
text = f.read().upper()

def next_capital(a, offset):
	b = ''
	temp = ord(a)
	temp -= 65
	temp += offset
	temp = temp%26
	temp += 65
	b = chr(temp)
	return b

def caesar(text, offset):
	solution = ''
	for s in text:
		if s == ' ':
			solution += ' '
		else:
			solution += next_capital(s, offset)
	return solution

for i in range(1, 26):
	print caesar(text, i)
