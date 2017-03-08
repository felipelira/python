#!/usr/bin/env python

# Felipe Lira Jan/2017 
#
#	From a genomic file (NCBI format), creates a description file to use as mapping file
#
#	usage: fasta2mapping.py fasta.file > output.txt


import sys
from Bio import SeqIO

dict = {}


file = open(sys.argv[1], "r")

# retrieve the sequence ID
for i in SeqIO.parse(file, "fasta"):
	ID = i.id
	ID_corrected = ID.split("|")[0] + "|" + ID.split("|")[1] + "|" + ID.split("|")[2]  + "|" + ID.split("|")[3] + "|"
	length = len(i.seq)
	desc = i.description
	desc_corrected = desc.replace(", complete sequence", "").replace(", complete CDS", "").replace(", complete genome", "")
	description = desc_corrected.split("|")[4]
	taxa = desc_corrected.split("|")[-1]
	dict[ID_corrected] = [str(length), taxa]

for i, j in dict.iteritems():
	print i +"\t"+ str("\t".join(j))
