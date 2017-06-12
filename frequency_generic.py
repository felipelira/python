#!/usr/bin/env python
# Felipe Lira 2017
# calculate frequency from BLAT tabular results

import sys
from collections import Counter

file = open(sys.argv[1]) # input file may be the output from bhit.py

list = []
for line in file:
	name = line.strip().split("\t")[1]
	list.append(name)

#print "Subject_sequence"+"\t"+"Frequency"

for i in Counter(list).most_common():
	print i[0]+"\t"+ str(i[1])
