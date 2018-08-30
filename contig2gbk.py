# !/usr/bin/env python

"""
Extract contigs from .gbk files and sabe in .gbk format.
For each ID, the script will created a separated contig file.

The script was created to extract plasmid contigs identified using 'extract_plasmids_from_report.py'

Usage:	contig2gbk.py [contig_ID|list_of_ID]

		Single contig:	contig2gbk.py -c NC_010694.1 -g GCF_000026185.1.gbff
		Contig list:	contig2gbk.py -c NC_010694.1,NC_010695.1 -g GCF_000026185.1.gbff

"""

from Bio import SeqIO
#from Bio.SeqUtils.CheckSum import seguid
import sys, os, argparse
from argparse import RawTextHelpFormatter

program = 'contig2gbk.py'

def get_arguments():
	parser = argparse.ArgumentParser(prog = program, usage= '\n\t%(prog)s [contig ID/ or list of contigs] [output prefix]' , description = "Split a .gbk (.gbff) file and retrieve the information of the contig of interest.",formatter_class=RawTextHelpFormatter)
	parser.add_argument('-c', required = False, type = str, help='Single contig (e.g. NC_010697.1) or list of contigs to be extracted separated by commas (e.g. NC_010697.1,NC_010693.1).', metavar='')
	parser.add_argument('-g', required = True, type = str, help='Genome file (.gbk) from which contigs will be extracted', metavar='') # when using a single genome, -g is the name of genome file in .gbk (.gbff) format
	#parser.add_argument('-o', required = False, type = str, help='Name of output file', metavar='')
	return parser


def main():
	d = {}
	parser = get_arguments()
	args = parser.parse_args()

	if args.c and args.g:

		ids = (args.c).split(',')

		with open(args.g, "rU") as genome:

			if len(ids) == 1:

				for x in ids:

					for record in SeqIO.parse(genome, "genbank"):

						if x == record.id:

							SeqIO.write([record], open(record.id + ".gbk", "w"), "genbank")

			elif len(ids) > 1:

				#ids = (args.c).split(',')
				for x in ids:

					for record in SeqIO.parse(genome, "genbank"):

						if record.id in ids:

							SeqIO.write([record], open(record.id + ".gbk", "w"), "genbank")
