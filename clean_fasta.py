# !/usr/bin/env python

from Bio import SeqIO
import sys
import os
import argparse

def get_arguments():
	parser = argparse.ArgumentParser(prog = 'clean_fasta.py', usage= '\n\t%(prog)s -i [input_file]')
	parser.add_argument('-i', required = True, type = str, help='Input file in fasta format.', metavar='--input')
	parser.add_argument('-o', required = True, type = str, help='out file in fasta format.', metavar='--output')
	return parser

def main():

	parser = get_arguments()
	args = parser.parse_args()

	with open(args.o, "w") as cleaned:

		with open(args.i, "rU") as fasta:

			for record in SeqIO.parse(fasta, "fasta"):

				if len(record.seq) == 0:
					pass
				else:
					cleaned.write('>' + record.description + '\n' + str(record.seq) + '\n' )


if __name__ == '__main__':
	main()
