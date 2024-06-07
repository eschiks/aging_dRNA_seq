#!/usr/bin/env python3

import sys

# convert consistent txt files into bed for browser tracks
with open(sys.argv[1]) as sites:
    with open(sys.argv[2],'w') as out_bed:
        for line in sites:
            line=line.strip().split()
            chrom,site,strand=line[0],line[1],line[2]
            start=str(int(site)-1)
            end=site
            name,score='psU',line[3]
            bed=[chrom,start,end,name,score,strand]
            out_bed.write('\t'.join(bed)+'\n')