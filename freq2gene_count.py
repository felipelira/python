  GNU nano 2.2.6                    File: freq2gene_count.py                                              

#!/usr/bin/env python
# Felipe Lira
# Concatenate the values obtained with frequency.py
# Pipeline resfinder

# Usage: freq2gene_count.py frequency.file > outfile

import sys

d = {}
d_tmp = {}

freq = open(sys.argv[1])

for line in freq:
        query  = line.strip().split("\t")[0]
        gene = query.split("_")[0]
        count = int(line.strip().split("\t")[1])
        if gene not in d:
                d[gene] = [count]
        else:
                d[gene].append(count)

#temporary dictionary
for s, t in d.iteritems():
        d_tmp[s] = sum(t)

for j, k in d_tmp.iteritems():
        print j +"\t"+ str(k)

