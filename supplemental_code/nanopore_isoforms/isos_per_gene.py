#!/usr/bin/env python3

import sys

day=str(sys.argv[1])

one=0
two=0
three=0
four=0
five_plus=0

isos_per={}

if day=='all':
    with open(sys.argv[2], 'r') as counts_file:
        for line in counts_file:
            if line[0]=='ids': # skip first line
                continue
            line=line.rstrip().split('\t') 
            gene=line[0][line[0].rfind('_')+1:]
            if gene not in isos_per:
                isos_per[gene]=1
            else:
                isos_per[gene]+=1
else:
    with open(sys.argv[2], 'r') as counts_file:
        for line in counts_file:
            line=line.rstrip().split('\t')
            if line[0]=='ids': # skip first line
                continue
            gene=line[0][line[0].rfind('_')+1:]
            if day=='day1': # pull counts from first 3 columns
                counts=float(line[1])+float(line[2])+float(line[3])
            else:
                counts=float(line[4])+float(line[5])+float(line[6])
            if counts>0 and gene not in isos_per:
                isos_per[gene]=1
            elif counts>0 and gene in isos_per:
                isos_per[gene]+=1
                    
for gene in isos_per:
    counts=isos_per[gene]
    if counts==1:
        one+=1
    elif counts==2:
        two+=1
    elif counts==3:
        three+=1
    elif counts==4:
        four+=1
    elif counts>=5:
        five_plus+=1

print(day+'\t'+str(one)+'\t'+str(two)+'\t'+str(three)+'\t'+str(four)+'\t'+str(five_plus))