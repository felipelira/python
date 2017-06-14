  GNU nano 2.2.6                                                       File: resfinder2mapping.py                                                                                                          Modified  

#!/usr/bin/env python
# Felipe Lira 2017
# created to include in the pipeline for metagenomic analysis to detect antimicrobial resistance genes
# Merge the information from the .fasta file and the "notes.txt" file provided by resfinder.
# All sequences were concatenated into a unique file and further their names were 

# Usage: resfinder2mapping.py fasta.file notes.txt

import sys
from Bio import SeqIO
import time

fasta_file = open(sys.argv[1], "r")
notes = open(sys.argv[2], "r")
d = {}
d_notes = {}
new_dict = {}

for sequence in SeqIO.parse(fasta_file, "fasta"):
        name = sequence.id#.replace("'", "")
        gene = name.split("_")[0]
        number = name.split("_")[1]
        gi = name.split("_")[2]
        seqlen = len(sequence.seq)
        AA = sequence.seq
        d[gene] = [name, number, gi, str(seqlen), AA]

for note in notes:
        gene_notes = note.split(":")[0]#.replace("'", "")
        resistance = note.split(":")[1].replace(" resistance", "")
        info = note.split(":")[2]
        d_notes[gene_notes] = resistance

for x , y in d.iteritems():
        for k, v in d_notes.iteritems():
                if k == x:
                        d[x].append(d_notes[x])
                        d[x].append(k)
                        new_dict[x] = d[x]
                        
print "# Table created by resfinder2mapping.py using the file " + str(sys.argv[1]) + " at " +  time.strftime("%d/%m/%Y") 
print "#Gene_name      Seq_name        Number  Accession_number      Length     Resistance      Gene"
for l , m in new_dict.iteritems():
        print l +"\t"+ '\t'.join(m)


