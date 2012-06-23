import os
import sys

# standard values
filename = ""
keyword = ""
margin = 30

# command line arguments
arg = sys.argv
if len(arg) == 3:
    filename = arg[1]
    keyword = arg[2]
elif len(arg) == 4:
    filename = arg[1]
    keyword = arg[2]
    margin = arg[3]
else:
    print "Please use as follows: match.py <filename> <keyword> [<margin>]"
    print "For example: match.py text.txt bloomsbury 45"
    os._exit(1)

# open file
f = open(filename, 'r')
text = f.read()

text = text.replace("\n", " ")
searchText = str(text)

# first occurence
pos = text.find(keyword)

# buils dummy
dummy = ""
for i in range(0, len(keyword)):
    dummy += "x"

# search for occurences
while ( pos != -1):
    print text[pos - 30 : pos + 30 + len(keyword)], "", pos
    searchText = searchText[:pos] + dummy + text[pos + len(keyword):]
    pos = searchText.find(keyword)
