#!/usr/bin/env python
# Felipe Lira 2017
# Created to merge the results of the frequency of genes presente in the blast_bhit.py table

import sys
import operator

frequency = open(sys.argv[1])

dict_count = {}
to_sort = {}
sorted_count = sorted(to_sort.items(), key=operator.itemgetter(1))


for line in frequency:
	item = line.strip().split("\t")[0]
	id = item.split("|")[0]
	name = item.split("|")[1]
	count = float(line.strip().split("\t")[1])
#	print id, name, count
	if name not in dict_count:
		dict_count[name] = [count]
	else:
		dict_count[name].append(count)


for k, v in dict_count.iteritems():
	K = k
	V =  str(sum(v))
	print k + "\t" + V
