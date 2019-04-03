#!/usr/bin/env python
from Bio import SeqIO
import sys
import os
import zipfile

# uses the name of the input file to create the output folder where the files will be stored
out_dir = sys.argv[1] + '_output'
os.mkdir(out_dir)
# read the multifasta file
fasta_sequences = SeqIO.parse(open(sys.argv[1]),'fasta')

for rec in fasta_sequences:
	id = rec.id
	seq = rec.seq
	id_file = open(os.path.join(out_dir,id + '.fasta' ), "w") 
	new_sequence = ">"+str(rec.description)+"\n"+str(seq)
	id_file.write(new_sequence)
	id_file.close()
fasta_sequences.close()

# zip files
zf = zipfile.ZipFile( out_dir + ".zip" , "w")
for dirname, subdirs, files in os.walk(out_dir):
    zf.write(dirname)
    for filename in files:
        zf.write(os.path.join(dirname, filename))
zf.close()
