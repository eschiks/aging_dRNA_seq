#!/usr/bin/env python3

import sys

# pull high confidence sites and reorganize output file

# 1 = prediction.csv, 2 = outfile name

with open(sys.argv[2],'w') as outfile:
    with open(sys.argv[1]) as prediction:
        for line in prediction:
            line=line.strip().split(',')
            if line[5]=='prob_modified':
                continue
            if float(line[5])>=0.9 and line[2]=='T': # can change value here to be more or less stringent
                chrom=line[0][:line[0].find('_')]
                if line[0][line[0].find('_')+1:]=='F':
                    strand='+'
                else:
                    strand='-'
                prob,coord,coverage=line[5],line[1],line[3]
                add=[chrom,coord,strand,prob,coverage]
                outfile.write('\t'.join(add)+'\n')