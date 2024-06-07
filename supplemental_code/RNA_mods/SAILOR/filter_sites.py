#!/usr/bin/env python3

import sys

with open(sys.argv[1]) as file:
    basename=file[:file.rfind('_')]
    out=basename+'_filtered_sites.bed'
    with open(out,'w') as outfile:
        with open(file) as sites:
            for line in sites: 
                line=line.strip().split()
                confidence=float(line[3])
                edited,total=float(line[4].split(',')[0]),float(line[4].split(',')[1])
                if edited/total>=0.05 and confidence>=0.75 and total>=20:
                    out=[line[0],line[1],line[2],str(edited/total),str(total),line[5]]
                    outfile.write('\t'.join(out)+'\n')   