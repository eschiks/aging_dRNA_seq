#!/usr/bin/env python3

replist=[]
with open('replist.txt') as reps:
    for line in reps:
        line=line.strip()
        replist.append(line)

tpm_list={}

for idx,rep in enumerate(replist):
    name=rep+'_iso_tpm.txt'
    with open(name) as tpm:
        for line in tpm:
            line=line.strip().split()
            if line[0]==rep:
                continue
            else:
                iso,exp=line[0],line[1]
                if iso not in tpm_list:
                    add=[float(0)]*24
                    add[idx]=float(exp)
                    tpm_list[iso]=add
                else:
                    current=tpm_list[iso]
                    current[idx]=float(exp)
                    tpm_list[iso]=current

with open('iso_counts_all_reps.txt','w') as outfile:
    outfile.write('\t'.join(replist)+'\n')
    for iso in tpm_list:
        add=[iso]
        for i in tpm_list[iso]:
            add.append(str(i))
        outfile.write('\t'.join(add)+'\n')