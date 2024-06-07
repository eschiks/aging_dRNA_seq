#!/usr/bin/env python3

times=['old','young']

for time in times:
    reps=[time+'_rep1_AG_filtered_sites.bed',time+'_rep2_AG_filtered_sites.bed',time+'_rep3_AG_filtered_sites.bed']
    rep1=[]
    rep2=[]
    rep3=[]
    for rep in reps:
        with open(rep) as bed:
            for line in bed:
                line=line.strip().split()
                del(line[3:5])
                if 'rep1' in rep:
                    rep1.append(tuple(line))
                elif 'rep2' in rep:
                    rep2.append(tuple(line))
                else:
                    rep3.append(tuple(line))
    one=[]
    two=[]
    three=[]
    for x in rep1:
        if x in rep2 and x in rep3:
            three.append(x)
        elif x in rep2 and x not in rep3:
            two.append(x)
        elif x in rep3 and x not in rep2:
            two.append(x)
        else:
            one.append(x)
    for x in rep2:
        if x not in rep3 and x not in rep1:
            one.append(x)
        if x in rep3 and x not in rep1:
            two.append(x)
    for x in rep3:
        if x not in rep1 and x not in rep2:
            one.append(x)
    outname=time+'_supporting_reps.txt'
    with open(outname,'w') as outfile:
        for site in one:
            info=list(site)
            info.append('1')
            outfile.write('\t'.join(info)+'\n')
        for site in two:
            info=list(site)
            info.append('2')
            outfile.write('\t'.join(info)+'\n')
        for site in three:
            info=list(site)
            info.append('3')
            outfile.write('\t'.join(info)+'\n')