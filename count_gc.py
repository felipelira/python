#!/usr/bin/env python

import sys
from Bio import SeqIO

filename=sys.argv[1]

fh= open(filename,'r')

parser = SeqIO.parse(fh, "fasta")

for record in parser:
	c=0
	a=0
	g=0
	t=0
	for x in str(record.seq):
		if "C" in x:
			c+=1    
		elif "G" in x:
			g+=1
		elif "A" in x:
			a+=1    
		elif "T" in x:
			t+=1
gc_content=(g+c)*100/(a+t+g+c)

print "%s\t%.2f" % (filename, gc_content)
