#!/usr/bin/env python

import sys
import re

data = open(sys.argv[1]).read()
ta_fix = re.sub(r'\(\d+\)','', data)

# change the names of the Phyla that don't have a concret classification.
data_fix = re.sub(r'Bacteria;Phylum1;unclassified;unclassified;unclassified;unclassified;', 'Bacteria;Phylum1;Phylum1_class;Phylum1_order;Phylum1_family;Phylum1_genus;', data_fi
x)
data_fix = re.sub(r'Bacteria;Phylum2;unclassified;unclassified;unclassified;unclassified;', 'Bacteria;Phylum2;Phylum2_class;Phylum2_order;Phylum2_family;Phylum2_genus;', data_fix)

print data_fix
