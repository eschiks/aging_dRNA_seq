#!/usr/bin/env python3

# compare unique FLAIR UTR coordinates to gtf 3'UTR annotation from Wormbase

def find_tx_id(x):
	start = x.index('transcript_id') + len('transcript_id')+2
	start_to_end = x[start:]
	end = start_to_end.index(';')-1
	return start_to_end[:end]



# make dictionary of annotated 3'UTRs from gtf - must be sorted for this approach to work

gtf_utrs={}

with open('c_elegans.PRJNA13758.WS279.canonical_geneset.sorted.gtf') as gtf:
	for line in gtf:
		line = line.strip().split('\t')
		feature=line[2]
		if feature == 'three_prime_utr':
			chrom,start,end,strand,tx_id=line[0],str(int(line[3])-1),line[4],line[6],find_tx_id(line[8]) # add 1 to start for 1-based indexing of gtf
			if tx_id not in gtf_utrs:
				gtf_utrs[tx_id]=[chrom,strand,start,end]
			else:
				add=[start,end]
				gtf_utrs[tx_id].extend(add)
		else:
			continue	

bed_utrs={}

# make dictionary of annotated 3'UTRs from UTR bed6 - must be sorted for this approach to work
with open('flair_10p_filtered_utrs.bed6') as bed:
	for line in bed:
		line = line.strip().split('\t')
		isoform,chrom,strand,start,end=line[3],line[0],line[5],line[1],line[2]
		if isoform not in bed_utrs:
			bed_utrs[isoform]=[chrom,strand,start,end]
		else: # if same UTR spans multiple exons
			add=[start,end]
			bed_utrs[isoform].extend(add) 

# combine isoforms that have the same 3'UTRs

unique_dict={}

for key in bed_utrs:
	coords=tuple(bed_utrs[key])
	isoform=key
	if coords not in unique_dict: # add coordinates of 3'UTR to dictionary as key
		unique_dict[coords]=[isoform]
	else:
		unique_dict[coords].append(isoform)

		
condensed_dict={}
for key in unique_dict:
	isoforms=tuple(unique_dict[key])
	condensed_dict[isoforms]=key # now this has UTR coordinates for genes that share the same UTRs
		
for k,value in condensed_dict.items():
	if value[1]=='-':
		list_to_add=[]
		create_range=range(int(value[2])-10,int(value[2])+11) # create start range 
		for x in create_range:
			g=list(value)
			g[2]=str(x)
			list_to_add.append(g[:])
		value=list_to_add
	if value[1]=='+':
		list_to_add=[]
		create_range=range(int(value[-1])-10, int(value[-1])+11)
		for x in create_range:
			g=list(value)
			g[-1]=str(x)
			list_to_add.append(g[:])
	condensed_dict[k]=list_to_add

compare_dict={}
counter=1

for key1, value1 in condensed_dict.items():
	utr_list=[]
	for utr in value1:
		for key2, value2 in gtf_utrs.items():
			if value2 == utr:
				utr_list.append(key2)
	if not utr_list:
		add='not_annotated_'+str(counter)
		counter+=1
		utr_list.append(add)
	compare_dict[key1]=utr_list
	
with open('WB_compare_utrs_new.tsv', 'w') as outfile:
	for key in compare_dict:
		isoform=list(key)
		utr=compare_dict[key]
		outfile.write(",".join(isoform)+'\t'+",".join(utr)+'\n')

