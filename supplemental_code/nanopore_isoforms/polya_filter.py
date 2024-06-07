#!/usr/bin/env python3

import sys
polya_set=set()

with open(sys.argv[1], "r") as polya:
        for line in polya:
                line=line.rstrip().split('\t')
                if line[9]=="PASS":
                        polya_set.add(line[0])

with open(sys.argv[3], 'w') as outfile:
    with open(sys.argv[2],'r') as bed:
            for line in bed:
                    x=line.rstrip().split('\t')
                    if x[3] in polya_set:
                            outfile.write('\t'.join(x)+'\n')