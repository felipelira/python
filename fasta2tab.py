#!/usr/bin/env python
# Felipe Lira Jan/2017 
#	Convert a .fasta file to table
#	usage: fasta2tab.py fasta.file > output.txt

import sys
from Bio import SeqIO

dict = {}

file = open(sys.argv[1], "r")

# retrieve the sequence ID
for i in SeqIO.parse(file, "fasta"):
	ID = i.id
	seq = i.seq
	dict[ID] = seq

for k, v in dict.iteritems():
	print k + "\t" + v
