  GNU nano 2.2.6                                                File: /bin/transpose.py                                                                                              Modified  

#!/usr/bin/python

# Created by Felipe Lira - the first will always be the first
# transpose ROWS to COLUMNS
# usage transpose.py [input_file] [output_file]

# Example:

#Letter Number
#A      1
#B      2
#C      3
#D      4

#Letters A B C D
#Numbers 1 2 3 4

import csv
import sys

def usage():
    print "\n Usage: transpose.py [infile] [out_file] \n".format(sys.argv[0])
    sys.exit()

if len(sys.argv) < 3:
    usage()

with open(sys.argv[1]) as i:
    rows = csv.reader(i, delimiter='\t', skipinitialspace=True)
    transposed_rows = zip(*rows)
    with open(sys.argv[2], 'w') as out:
        w = csv.writer(out, delimiter='\t')
        w.writerows(transposed_rows)
