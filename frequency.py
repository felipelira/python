#!/usr/bin/env python
# created by Felipe Lira Feb/2017
# to calculate frequency from BLAST tabular results
# based on subject column
# useful to calculate the frequency for any 
# table with two or more columns.

import sys
from collections import Counter

file = open(sys.argv[1])

list = []
for line in file:
        name = line.strip().split("\t")[1]
        name_correct = name.split("|")[0] + "|" + name.split("|")[1] + "|" +  name.split("|")[2] + "|" +  name.split("|")[3]+"|"
        list.append(name_correct)

for i in Counter(list).most_common():
        print i[0]+"\t"+ str(i[1])

