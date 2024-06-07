#!/usr/bin/env python3

import sys

def average(lst):
    return sum(lst) / len(lst)

path_list=[sys.argv[1],sys.argv[2],sys.argv[3]]

rep1=set()
rep2=set()
rep3=set()

percent_dict={}
read_dict={}

for x in path_list:
    with open(x) as rep:
        for line in rep:
            line=line.strip().split()
            add=line[0:3]
            add.append(line[5])
            add=tuple(add)
            if x==sys.argv[1]:
                rep1.add(add)
            elif x==sys.argv[2]:
                rep2.add(add)
            else:
                rep3.add(add)
            if add not in percent_dict:
                percent_dict[add]=[float(line[4])]
            else:
                percent_dict[add].append(float(line[4]))
            if add not in read_dict:
                read_dict[add]=int(line[3].split(',')[1])
            else:
                read_dict[add]+=int(line[3].split(',')[1])

out=list(rep1.intersection(rep2,rep3))

mean_percent={}

for x in percent_dict:
    mean_percent[x]=str(average(percent_dict[x]))

with open(sys.argv[4],'w') as outfile:
    for x in out:
        search=tuple(x)
        x=list(x)
        if search in mean_percent and search in read_dict:
            mean=str(round(float(mean_percent[search]),2))
            reads=str(read_dict[search])
        x.append(mean)
        x.append(reads)
        out=[x[0],x[1],x[2],x[4],x[5],x[3]]
        outfile.write('\t'.join(out)+'\n')