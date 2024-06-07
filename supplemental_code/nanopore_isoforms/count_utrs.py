#!/usr/bin/env python3

import sys

anno=set()
novel=set()
with open('WB_compare_utrs_new.tsv') as utrs:
    for line in utrs:
        line=line.strip().split('\t')
        isos=line[0].split(',')
        if 'not_annotated' in line[1]:
            for x in isos:
                novel.add(x)
        else:
            for x in isos:
                anno.add(x)
                
day=str(sys.argv[1])

anno_counts=0
novel_counts=0
total=0

if day=='all':
	with open(sys.argv[2], 'r') as counts_file:
		for line in counts_file:
			line=line.rstrip().split('\t')
			if line[0] in anno: # annotated utr
				total+=1
				anno_counts+=1
			elif line[0] in novel: # novel utr
				total+=1
				novel_counts+=1
else:
	with open(sys.argv[2], 'r') as counts_file:
		for line in counts_file:
			line=line.rstrip().split('\t')
			if line[0]=='ids': # skip first line
				continue
			if day=='day1': # pull counts from first 3 columns
				counts=float(line[1])+float(line[2])+float(line[3])
			else:
				counts=float(line[4])+float(line[5])+float(line[6])
			if line[0] in anno and counts>0: 
				total+=1
				anno_counts+=1
			elif line[0] in novel and counts>0: 
				total+=1
				novel_counts+=1

print(day+'\t'+str(total)+'\t'+str(anno_counts)+'\t'+str(novel_counts))
