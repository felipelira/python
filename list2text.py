#!/usr/bin/env python

import sys

mylist= open(sys.argv[1], "r")

mytext = set()

for line in mylist:
        item = line.strip()
        mytext.add(item)

print ' '.join(mytext)

# print ', '.join(mytext) # in the cae you need commas instead of spaces.
