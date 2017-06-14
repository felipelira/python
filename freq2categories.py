#!/usr/bin/env python
# Felipe Lira 2017
# Resfinder pipeline - step 4
# Merge the information contained in the frequency.pl (*.freq) and assign one category
# based on the resfinder.mapping.txt

# Usage: freq2categories.py frequency.file mapping.file > output.file
# 'frequency.file' = file obtained by frequency.py
# 'mapping.file' = file containing all the information about the genes in the database used to perform the BLAST

# Frequency.file example
# tet(Q)_1_L33696	142
# tet(Q)_4_Z21523	54
# tet(W)_6_FN396364	53
# msr(E)_4_EU294228	38
# strA_5_AF321550	28
# tet(O)_3_Y07780	25

# Mapping.file example
# #ID	Name	Resistance	Order	GI	length
# aac(2')-Ia_1_L06156	aac(2')-Ia	Aminoglycoside resistance	1	L06156	537
# aac(2')-Ib_1_U41471	aac(2')-Ib	Aminoglycoside resistance	1	U41471	588
# aac(2')-Ic_1_U72714	aac(2')-Ic	Aminoglycoside resistance	1	U72714	546
# aac(2')-Id_1_U72743	aac(2')-Id	Aminoglycoside resistance	1	U72743	633

import sys

d = {}
d_tmp = {}
d_map = {}
new_dict = {}

freq = open(sys.argv[1])
mapping_file = open(sys.argv[2])

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

#for j, k in d_tmp.iteritems():
#	print j +"\t"+ str(k)

for line in mapping_file:
	if not line.startswith("#"):
		gene  = line.strip().split("\t")[1]	
		category = line.strip().split("\t")[2]
		d_map[gene] = category

for k, v in d_tmp.iteritems():
	for l, m in d_map.iteritems():
		if l == k:
			if d_map[k] not in new_dict:
				new_dict[d_map[k]] = [v]
			else:
				new_dict[d_map[k]].append(v)

#print {k:sum(v) for k,v in new_dict.items()}
for k, v in new_dict.iteritems():
	print k +"\t"+ str(sum(v))
