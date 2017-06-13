#!/usr/bim/env python
# Merge the results from a table into the same gene name

# For example
# YP_006374661.1|EF-Tu	4
# AAB39605.1|EF-Tu	3
# NP_312937.1|rpoB	2
# AAK44936.1|rpsL	2
# AAR89358.1|TEM-127	1

# After merging the values by the name of the genes, we have this:
# EF-Tu  7
# rpoB  2
# rpsL 2
# TEM-127  1


import sys

frequency = open(sys.argv[1])
dict_count = {}

for line in frequency:
	item = line.strip().split("\t")[0]
	id = item.split("|")[0]
	name = item.split("|")[1]
	count = float(line.strip().split("\t")[1])
	if name not in dict_count:
		dict_count[name] = [count]
	else:
		dict_count[name].append(count)


for k, v in dict_count.iteritems():
	K = k
	V =  str(sum(v))
	print k + "\t" + V
