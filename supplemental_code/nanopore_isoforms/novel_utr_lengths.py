#!/usr/bin/env python3

novel=set()
with open('WB_compare_utrs_new.tsv') as utrs:
    for line in utrs:
        line=line.strip().split()
        if 'not_annotated' in line[1]:
            novel.add(line[0])
        
length_dict={}

with open('novel_utr_lengths.txt','w') as outfile:
    with open('utr_lengths.txt') as utr_lengths:
        for line in utr_lengths:
            line=line.strip().split()
            if line[0] in novel:
                outfile.write('\t'.join(line)+'\n')
            
        