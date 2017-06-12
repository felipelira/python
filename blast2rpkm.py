#!/usr/bin/env python

import sys
from Bio import SeqIO

# Calculates the RPKM values using a BLAST tabular output 
# It needs one table with the best BLAST hit for each read, and
# one '.fasta' file with the references from database (to calculate the length of sequences)

# usage: blast2rpkm.py <bhit_blast.py> <reference_file.fasta>

file = open(sys.argv[1], "r") # output bhit_blast.py
fasta_file = open(sys.argv[2], "r")# length of blast subject sequences

parse = SeqIO.parse(fasta_file, "fasta")

dict = {}	# dictionary with the length of mapped nucleotides from reads according the tabular file from BLAST
dict_len = {}	# dictionary with the length of the protein sequences
new_dict = {}	# corrected dict{} containing the total of nucleotides mapped against reference sequence


for line in file:
	id = line.split("\t")[1]
	match_cov = int(line.split("\t")[3])*3 # mapped coverage multiplied by three to obtains the length in nucleotides
	if id not in dict:
		dict[id] = [match_cov]
	else:
		dict[id].append(match_cov)

for k , v in dict.iteritems():
	new_dict[k] = sum(v)

for record in parse:
	seq_name = record.id.split("|")[0] +"|"+ record.id.split("|")[1] +"|"+ record.id.split("|")[2] +"|"+record.id.split("|")[3] +"|"
	dict_len[seq_name] = str(len(record.seq)*3) # it considers the length of the nucleotide sequence

#for y , z in dict_len.iteritems():
#	print y, z

for x , y in new_dict.iteritems():
	for k , l in dict_len.iteritems():
		if x == k:
			print x, (float(dict_len[x])/float(new_dict[x])), new_dict[x])
