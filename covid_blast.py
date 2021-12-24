#! usr/bin/env python

"""
It performs a blast alingnmentand retrieve your results based on a customized identity and coverage.
"""

import subprocess
import os
import sys


# indicate here the PATH to your file
infile = "/home/flira/scripts/prot_seqs_test.faa"
#set_infile = sys.argv[1]

# Set the PATH to your database
dict_db = {blastp:"PATH/to/protein/database", blastn:"PATH/to/nucleotide/database"}

def main(infile, db):
    
    identity = float(input("Set the identity: "))
    coverage = float(input("Set the coverage: "))
    blast = input("Choose your BLAST [blastn / blastp]: ")
    
    temp_blast = "./temp_blast.txt"

    command_line = [dict_db(blast) ,'-query', infile, '-outfmt', '6 qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore qlen slen','-db', db, '-out', temp_blast]

    subprocess.call(command_line)

    for line in open(temp_blast):
           
        l = line.strip().split("\t")
        
        alignment, query_len = int(l[3]), int(l[12])

        if float(alignment / query_len)*100 >= coverage and float(l[2]) >= identity: #  and float(alignment/query_len) >= 0.85:
            
            print("Coverage", round(100*(alignment/query_len), 2) , "%" )
            
            print( "\t".join(line.strip().split("\t") ))



if __name__ == "__main__":
    main(infile, db)
