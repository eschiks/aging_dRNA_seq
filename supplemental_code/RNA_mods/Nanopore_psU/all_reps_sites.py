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
            add=tuple(line[0:3])
            if x==sys.argv[1]:
                rep1.add(add)
            elif x==sys.argv[2]:
                rep2.add(add)
            else:
                rep3.add(add)
            if add not in percent_dict:
                percent_dict[add]=[float(line[3])]
            else:
                percent_dict[add].append(float(line[3]))
            if add not in read_dict:
                read_dict[add]=int(line[4])
            else:
                read_dict[add]+=int(line[4])

out=list(rep1.intersection(rep2,rep3))

mean_percent={}

for x in percent_dict:
    mean_percent[x]=str(average(percent_dict[x]))

chrom_sizes={}

with open(sys.argv[4]) as sizes:
    for line in sizes:
        line=line.strip().split()
        chrom_sizes[line[0]]=int(line[1])

final_out=[]

conversion={}

for x in out:
    y=list(x)
    chrom,site,strand=x[0],x[1],x[2]
    if strand=='-':
        new_site=str(chrom_sizes[chrom]-int(site))+1 
        y[1]=new_site
    final_out.append(y)
    conversion[tuple(y)]=tuple(x)

for x in final_out:
    search=tuple(x)
    if search in mean_percent and search in read_dict:
        mean=str(round(float(mean_percent[search]),2))
        reads=str(read_dict[search])
    else:
        search_inverse=conversion[search]
        mean=str(round(float(mean_percent[search_inverse]),2))
        reads=str(read_dict[search_inverse])
    x.append(mean)
    x.append(reads)

with open(sys.argv[5],'w') as outfile:
    for x in final_out:
        outfile.write('\t'.join(x)+'\n')