#!/usr/bin/env python
# Felipe Lira 2016
# Recreates the contigs inserting those predicted genes/proteins 
# Contigs generated by Spades and predicted using Prodigal

# usage: genes_per_contigs.py [file.fasta] > output_file


import sys
from Bio import SeqIO

#file = SeqIO.parse(sys.argv[1], "fasta")
file = open(sys.argv[1], "r")
dict = {}

for sequence in file:
#	name = sequence.id
#	contig = name.split('_')[0]+'_'+name.split('_')[1]
#	direction = sequence.id.split('#')[3]
#	if contig not in dict:
#		dict[contig] = [name]
#	else:
#		dict[contig].append(name)

#for k, v in dict.iteritems():
#	print k+'\t'+ str(len(v))
#	if len(v) >= 2:
#	print k+'\t'+ str('\t'.join(v))
	if sequence.startswith(">"):
		name = sequence.strip().replace(">", "").split(" # ")
		contig = name[0].strip().split("_")[0]+"_"+name[0].strip().split("_")[1]+"_"+name[0].strip
().split("_")[2]+"_"+name[0].strip().split("_")[3]+"_"+name[0].strip().split("_")[4]+"_"+name[0].strip().s
plit("_")[5]
		direction = sequence.strip().split(" # ")[3]
		gene = name[0] # +"("+direction+")"
		if contig not in dict:
			dict[contig] = [gene]
		else:
			dict[contig].append(gene)
#		print gene
for k, v in dict.iteritems():
	#print k+'\t'+ str(len(v))
	if len(v) >= 2:
		print k+'\t'+ str('\t'.join(v))
