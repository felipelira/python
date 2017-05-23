#!/usr/bin/env python
# Felipe Lira 2017
# list2m8 retrieves the results from one sequence at m8 BLAST format.
# usage: list2m8.py list_file.txt BLAST_file.bhit

import sys

list = open(sys.argv[1])        # list containning the name of complete genes selected after prodigal prediction: "partial=00;"
blast = open(sys.argv[2])       # blast tabular result filtered by bhit_blast.py


genes = []      # list with complete genes names
                # these genes are used to retrieve the results from BLASTp hits
queries = {}    # dictionary with query and subjects results
best_query = [] # list containing predicted genes with best match query_vs_subject and subject_vs_query
                # they were selected througth two steps: 
                # 1st: the query sequences match with 95% of coverage and 90% of identity against reference database
                # 2nd: the query length corresponds to 95% of the subject length


for line in list:
        name = line.strip()
        genes.append(name)
#print genes
for result in blast:
        query = result.strip().split("\t")[0]
        match = result.strip().split("\t")[1:]
#print queries
        qlen = result.strip().split("\t")[8]
        slen = result.strip().split("\t")[11]
        percent = (float(qlen)/float(slen))*100
        if percent >= 95:       # adjust the percentage of coverage between query and subject
                                # al values equal or greater than this threshold are accecpted as a valid query sequence
                queries[query] = match

for k, v in queries.iteritems():
        best_query.append(k)
        print k + "\t" + ("\t").join(v)





