#!/usr/bin/env python3

# input bed12 file, output feature name with length. Used this to get feature lengths for 3'UTRs and Nanopore isoforms

import sys

with open(sys.argv[1], 'r') as bed:
    with open(sys.argv[2],'w') as outfile:
        outfile.write('feature' + '\t' + 'length' + '\n')
        for line in bed:
            line = line.strip().split('\t')
            length,name=sum(list(map(int, line[10].strip(',').split(',')))),line[3]
            outfile.write(name + '\t' + str(length) + '\n')
                          
        
