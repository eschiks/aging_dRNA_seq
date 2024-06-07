#!/usr/bin/env python3

import re

productivity=open('/expanse/lustre/scratch/eschiksn/temp_project/IAN_MAPPING/final_isoforms/isoform_productivity_new.bed')
productivity_out=open('/expanse/lustre/scratch/eschiksn/temp_project/IAN_MAPPING/final_isoforms/isoform_productivity_new_named.bed','w')

pro_counter_splice=0
unpro_counter_splice=0
pro_counter_SE=0
unpro_counter_SE=0
name_dict={}

for line in productivity:
    line=line.rstrip().split('\t')
    name=line[3]
    WB=name[name.rfind('_')+1:]
    if line[11]=='0,':
        if len(name)>=37:
            if name[36]=='_' or name[38]=='_':
                if line[12]=='PRO':
                    pro_counter_SE+=1
                    new_name='single_exon_productive_isoform'+'_'+str(pro_counter_SE)+'_'+WB
                else:
                    unpro_counter_SE+=1
                    new_name='single_exon_unproductive_isoform'+'_'+str(unpro_counter_SE)+'_'+WB
                line[3]=new_name
                name_dict[name]=new_name
            
    elif len(name)>=37:
        if name[36]=='_' or name[38]=='_':
            if line[12]=='PRO': # productive isoform 
                pro_counter_splice+=1
                new_name='productive_splice_isoform'+'_'+str(pro_counter_splice)+'_'+WB
            else:
                unpro_counter_splice+=1
                new_name='unproductive_splice_isoform'+'_'+str(unpro_counter_splice)+'_'+WB
            line[3]=new_name
            name_dict[name]=new_name
    productivity_out.write("\t".join(line)+"\n")

productivity.close()
productivity_out.close()
	
counts=open('flair.quantify.counts.tsv')
counts_out=open('flair.quantify.counts_named.tsv','w')

for line in counts:
    line=line.rstrip().split('\t')
    name=line[0]
    if name in name_dict:
        new_name=name_dict[name]
        line[0]=new_name
    counts_out.write("\t".join(line)+"\n")

counts.close()
counts_out.close()
	
isoforms_bed=open('collapse_10p_filtered.isoforms.bed')
out_bed=open('collapse_10p_filtered_named.isoforms.bed','w')

for line in isoforms_bed:
    line=line.rstrip().split('\t')
    if line[3] in name_dict:
        line[3]=name_dict[line[3]]
    out_bed.write("\t".join(line)+"\n")
	
isoforms_bed.close()
out_bed.close()

fasta=open('collapse_10p_filtered.isoforms.fa')
fasta_out=open('collapse_10p_filtered_named.isoforms.fa','w')
	
for line in fasta:
    if line.startswith('>'):
        name=line[1:-1]
        if name in name_dict:
            new_name=name_dict[name]
            newline='>'+new_name
            fasta_out.write(newline+'\n')
        else:
            fasta_out.write(line)
    else:
        fasta_out.write(line)

fasta.close()
fasta_out.close()