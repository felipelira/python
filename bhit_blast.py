#!/usr/bin/env python
# Felipe Lira 201
# Retrieve the best hit from a BLAST tabular result
# usage: bhit_blast.py BLAST_m8.tab > output.m8

import sys
from collections import Counter

file = open(sys.argv[1], "ru")
d = {}

for line in file:
        query = line.strip().split('\t')[0]
        data = line.strip().split('\t')[1:]
        if query not in d:
                d[query]= data

for k, v in d.iteritems():
        print k+'\t'+ str('\t'.join(v))
