#!/usr/bin/env python
# Felipe Lira 2016
# get_length.py multifasta_file
# retrieve the record and length of all fasta sequece in a multifasta file

import sys
from Bio import SeqIO

dict = {}

data = SeqIO.parse(sys.argv[1], "fasta")

for sequence in data:
	name_original = sequence.id
	name = name_original.split("|")[0] + "|" + name_original.split("|")[1] + "|" + name_original.split("|")[2] + "|" + name_original.split("|")[1] + "|"
	length = len(sequence.seq)
	dict[name] = length
 
for k, v in dict.iteritems():
    print k + "\t" + str(dict[k])
    #print k + "\t" + str(dict[k] *3)	# uncomment if you want to convert the protein length to nucleotide length
