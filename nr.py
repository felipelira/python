from Bio import SeqIO
import sys, os

"""usage:
	nr.py infile.fasta > outfile.fasta
"""

infile = sys.argv[1]

dict = {}

for record in SeqIO.parse(infile, "fasta"):
	if str(record.seq) not in dict:
		dict[str(record.seq)] = [record.id]
	else:
		dict[str(record.seq)].append(record.id)

for k, v in dict.items():
	if len(v) == 1:
		print(">" + "".join(v))
		print(k)
	else:
		# It prints the first name and the identical between '[]'
		print(">" + v[0] + "[" + v[1:] + "]")
		print(k)
