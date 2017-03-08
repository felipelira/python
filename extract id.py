#!/usr/bin/env python

# Felipe Lira Nov/2016

# Extract IDs from genes predicted using Prodigal
# Previous contigs created using Spades Assembler

# Predicted gene name:
# >NODE_1_length_789_cov_0.634783_1 # 3 # 788 # 1 # ID=1_1;partial=11;start_type=Edge;rbs_motif=None;rbs_spacer=None;gc_cont=0.665
# Output table:
# ORF   Gene_start      Gene_end        Orientation     ID(contig_gene) Prediction_type Start_type
# NODE_1_length_789_cov_0.634783_1      3       788     1       ID=1_1  partial=11      start_type=Edge

import sys

file = open(sys.argv[1], 'r')
dict_names={}

for line in file:
        name = line.replace(" # ", ";").replace(">", "").replace("start_type=","").replace("ID=", "").replace("partial=","").split(";")
        dict_names[name[0]] = name[1:7]
#       contig = name[0].split('_')[0]+'_'+ name[0].split('_')[1]

#print 'ORF'+'\t'+'Gene_start'+'\t'+'Gene_end'+'\t'+'Orientation'+'\t'+'ID(contig_gene)'+'\t'+'Prediction_type'+'\t'+'Start_type'

for k, v in dict_names.iteritems():
        print k+'\t'+ str('\t'.join(v))
