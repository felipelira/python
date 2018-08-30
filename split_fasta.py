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







inhandle = sys.argv[1] # file containing the fasta sequence which you want to extract
fasta = sys.argv[2] # name of the sequence to be extracted

parse = SeqIO.parse(open(inhandle, 'r'), "fasta")

for record in parse:
	if record.id == fasta:
		output = open(record.id + '.fasta', "w")
		sequence = '>' + record.description + '\n' + str(record.seq)
		output.write(sequence)
		output.close()#print sequence
