#!/usr/bin/env python
# Felipe Lira 2017
# calculate frequency from BLAST tabular results
# It uses the bhit.file

# frequency.py bhit.file > output.file

import sys
from collections import Counter

file = open(sys.argv[1])

list = []
dict = {}

for line in file:
        gi = line.strip().split("\t")[1]
        name = line.strip().split("\t")[2]
        list.append(gi)

for i in Counter(list).most_common():
        print i[0]+"\t"+ str(i[1])
