#!/usr/bin/env python

# created by Felipe Lira Jan/2017
# Normalize the number of mapped reads to Transcripts Per Millon (TPM)
# using a reference file containing the length of the nucleotide sequences
# and a frquency file with the values of mapped reads (obtained with frequency.py)
# To merge the names, is recommended to use the mapping file # exceptions

# usage: blast2tpm.py <frequency_file> <reference_file> <mapping_file>


import sys
from Bio import SeqIO
from collections import Counter

frequency = open(sys.argv[1], "r")
reference = open(sys.argv[2], "r")	# previously, create a length file using get_length.py
mapping_file = open(sys.argv[3], "r")

dict_freq = {}
dict_map = {}
dict_len = {}
mapped_reads = []
#factor = sum(mapped_reads)/1000000 #sum of all mapped reads/10^6 = scaling factor

# extract data from frequency table (output frequency.py)
for line in frequency:
	gene = line.strip().split("\t")[0]
	freq = line.strip().split("\t")[1]
	dict_freq[gene] = [freq]

# retrieve information from the 'mapping file' using the 'gene name' as query
# to create the dict_map
for row in mapping_file:
	gi = row.strip().split("\t")[4]
	gene = row.strip().split("\t")[2]
	dict_map[gi] = gene

# merge onformation from two dictionaries and complement the dict_freq
for k , v in dict_freq.iteritems():
	if k in dict_map:
		dict_freq[k].append(dict_map[k])
#print dict_freq

#include information about the lengtth of the gene
for sequence in reference:
	name = sequence.strip().split("\t")[0]
	length = float(sequence.strip().split("\t")[1])/1000	# x/1000 to obtain the value in Kb
	mapped_reads.append(length)
	dict_len[name] = length

for j , l in dict_freq.iteritems():
	if j in dict_len:
		dict_freq[j].append(dict_len[j])


factor = sum(mapped_reads)/1000000 #sum of all mapped reads/10^6 = scaling factor
#print factor
#print dict_freq
