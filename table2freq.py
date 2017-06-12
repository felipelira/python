  GNU nano 2.2.6                                                File: /media/disk4/felipe/scripts/table2freq.py                                                                                                      

#!/usr/bin/env python
# calculate frequency from BacMet tabular results (.table)
# similar to frequency.py

import sys
from collections import Counter

file = open(sys.argv[1])
length = open(sys.argv[2])

list = []
dict = {}
dict_len = {}

next(file)

for seq in length:
        seq_gi = seq.strip().split("\t")[0]
        seq_gi_correct = seq_gi.split("|")[0] + "|" +  seq_gi.split("|")[1] + "|" + seq_gi.split("|")[2] + "|" + seq_gi.split("|")[3] + "|"
        seq_len = seq.strip().split("\t")[1]
        dict_len[seq_gi_correct] = seq_len
#       print seq_gi_correct + "\t" + seq_len

for line in file:
        gi = line.strip().split("\t")[1]
        gi_correct = gi.split("|")[0] + "|" +  gi.split("|")[1] + "|" + gi.split("|")[2] + "|" + gi.split("|")[3] + "|"
        name = line.strip().split("\t")[2]
        list.append(name)
        if gi not in dict:
                dict[gi_correct] = name

for j, k in dict.iteritems():
        print j + "\t" + dict[j]
