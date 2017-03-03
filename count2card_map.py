  GNU nano 2.2.6                                                File: count2card_map.py                                                                                                        

#!/usr/bin/env python

# cross the information in count table (frequency.py output) with CARD mapping file
import sys

count_frequency = open(sys.argv[1])     # output from frequency.py

map = open("/media/disk4/felipe/2016/JPI/databases_JPI/CARD_GIs_2162.mapping.txt", "r")

list = []
dict_count = {}
dict = {}

next(count_frequency)
for line in count_frequency:
        id =  line.strip().split("\t")[0]
        list.append(id)
        count = line.strip().split("\t")[1]
        dict_count[id]=count

for gene in map:
        ID = gene.split("\t")[4]
        gene = gene.split("\t")[2]
        dict[ID] = gene

for name in list:
        for k, v in dict.iteritems():
                if name == k:
                        print name +"\t"+ dict[name]+"\t"+dict_count[name]
