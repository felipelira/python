  GNU nano 2.2.6                     File: bhit_by_coverage.py                                        Modified  

#!/usr/bin/env python
# Felipe Lira 2017

# created to include in the pipeline for metagenomic analysis to detect 
# antimicrobial resistance genes using Resfinder database

# blast.output (tabular BLAST) needs to be generated with this format:
  # qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore qlen slen

# Usage: bhit_by_coverage.py blast.output > outfile

import sys
from Bio import SeqIO

blast = open(sys.argv[1], "r")

d = {}

for line in blast:
        subject = line.strip().split("\t")[0]
        identity = float(line.strip().split("\t")[2])
        match_length = float(line.split("\t")[3]) # length of match
        qlen = float(line.split("\t")[12])
        info = line.strip().split("\t")[1:]
        min_coverage = float(match_length) / (qlen)

        # define value of converage to print the results. (Default= 0.90)
        # length >= 75 because it is the equivalent to 25 animo acids, the minimun length accepted

        if identity >= 90 and min_coverage >= 0.90: # and 0.90 * length >= 75:
                print subject +"\t"+ ('\t').join(info)
