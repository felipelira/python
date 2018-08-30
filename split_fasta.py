#!/usr/binenv python

# split_fasta.py [fasta.file]
# split sequences from a fasta file separating into different files

import sys
from Bio import SeqIO

inhandle = sys.argv[1]

#seqtype = sys.argv[2] # if faa or fna
parse = SeqIO.parse(open(inhandle, 'r'), "fasta")

for record in parse:
	output = open(record.id + '.' + seqtype, "w")
	sequence = record.description + '\n' + str(record.seq)
	output.write('>' + sequence)
	output.close()#print sequence
