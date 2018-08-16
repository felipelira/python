#!/usr/bin/env python

# csv2bin.py [input_name] [output_name]

import csv
import sys
import argparse
from argparse import RawTextHelpFormatter

def get_arguments():
	parser = argparse.ArgumentParser(prog = 'csv2bin.py', usage= '\n\t%(prog)s [roary.csv] [output_prefix]' , description = "Convert the presence/absence table from roary to a binary matrix (standard and transposed).",formatter_class=RawTextHelpFormatter)
	parser.add_argument('-i', required = True, type = str, help='Name of input file (mandatory)', metavar='')
	parser.add_argument('-o', required = True, type = str, help='Name of output file (mandatory)', metavar='')
	return parser.parse_args()


def main():
	args = get_arguments()	# check arguments

	with open(args.i, "rU") as fin , open(args.o + '.matrix','w') as fout:
		foutWriter = csv.writer(fout, delimiter='\t', escapechar=' ',quotechar='', quoting=csv.QUOTE_NONE)
		first = fin.readline().strip().split(',')
		count_strains = 14 + len(first[14:])
		strains = first[14:count_strains]
		desc = str("|".join(first[0:3])).replace('"', '')
		genomes = ",".join(first[14:count_strains])
		row = str(desc + "," + genomes).replace('"', '')
		foutWriter.writerow([row])
		for lines in fin:
			line = lines.strip().split(',')
			desc_gene = str("|".join(line[0:3])).replace('"', '')
			pres_abs = ",".join(['0' if x is '' else '1' for x in [x.replace('""', '') for x in line[14:count_strains]]])			
			gene_row = str(desc_gene + "," + pres_abs)
			foutWriter.writerow([gene_row])
		with open(args.o + '.matrix','r') as read_out , open(args.o + '_transposed.matrix','w') as tout:
			rows = csv.reader(read_out, delimiter=',', skipinitialspace=True)
			transposed_rows = zip(*rows)
			w = csv.writer(tout, delimiter='\t')
			w.writerows(transposed_rows)
		print 'Done!'

if __name__== "__main__":
	main()
