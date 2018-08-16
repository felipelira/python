# !/usr/bin/env python

from Bio import SeqIO
from Bio.SeqUtils.CheckSum import seguid
import sys
import os

#Usage: contig2genbank.py [list] [dicrectory]

"""
Example of list to be used as input:
1# column: accession of gbff file
2# column: names of contigs separated by commas

GCF_000026185.1	\t	NC_010695.1,NC_010696.1,NC_010699.1,NC_010693.1,NC_010697.1
GCF_000026985.1	\t	NC_017391.1,NC_017388.1,NC_017392.1,NC_017389.1
GCF_000027205.1	\t	NC_013972.1,NC_013973.1
GCF_000027265.1	\t	NC_013264.1,NC_013265.1,NC_013954.1,NC_013263.1

"""


input_file = sys.argv[1] # list with accession and contigs names
gbff_dir = sys.argv[2] # gbff file or directory containing gbff files
out_dir_contigs = os.path.join(gbff_dir.split('/')[-1]) + '_extracted_contigs'
out_dir_plasmids = os.path.join(gbff_dir.split('/')[-1]) + '_extracted_plasmids'


try:
	os.mkdir(out_dir_contigs)
except:
	pass

try:
	os.mkdir(out_dir_plasmids)
except:
	pass



dict_contig = {}
#dict_records = {}
dict_files = {}



input_handle = open(input_file, "rU")

for line in input_handle:
	accession = line.strip().split('\t')[0]
	contigs = line.strip().split('\t')[1].split(',')
	dict_contig[accession] = contigs

# store informations about contigs to be extracted and write to file


for k, v in dict_contig.iteritems():
	file_name = k + '.gbff'
	seguid_dict = SeqIO.to_dict(SeqIO.parse(os.path.join(gbff_dir, file_name), "genbank"), lambda rec: seguid(rec.seq))
	for key, value in seguid_dict.iteritems():
	#for key, info in seguid_dict.iteritems():
		record = seguid_dict[key]
		if record.id in v:
			out_gbk = os.path.join(out_dir_contigs,record.id) + '_contigs.gbk'
			SeqIO.write(record, out_gbk, "genbank")
			if k not in dict_files:
				dict_files[k] = [out_gbk]
			else:
				dict_files[k].append(out_gbk)
#print dict_files

for accession, filenames in dict_files.iteritems():
	out_gbk_file = open(os.path.join(out_dir_plasmids,accession) + '_plsm.gbk', 'w')
	print (os.path.join(out_dir_plasmids,accession) + '_plsm.gbk')
	for fname in filenames:
		with open(fname) as infile:
			for line in infile:
				out_gbk_file.write(line)
