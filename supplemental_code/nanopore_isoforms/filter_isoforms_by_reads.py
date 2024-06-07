#!/usr/bin/env python3

import sys

def split_gene_ids(x):
	gene=x[x.find('_')+1:]
	return gene

def grab_tx_id(x):
    start = x.index('transcript_id') + len('transcript_id')+2
    start_to_end = x[start:]
    end = start_to_end.index(';')-1
    return start_to_end[:end]

def grab_wb_id(x):
    start = x.index('gene_id') + len('gene_id')+2
    start_to_end = x[start:]
    end = start_to_end.index(';')-1
    return start_to_end[:end]

gene_counts={}
filter_set=set()
with open(sys.argv[1],'r') as reads:
	for line in reads:
		line=line.rstrip().split('\t')
		gene=split_gene_ids(line[0])
		read_number=float(len(line[1].split(',')))
		if gene not in gene_counts:
			gene_counts[gene]=read_number
		else:
			gene_counts[gene]+=read_number

with open(sys.argv[1],'r') as reads:
	for line in reads:
		line=line.rstrip().split('\t')
		iso=line[0]
		gene=split_gene_ids(line[0])
		read_number=float(len(line[1].split(',')))
		if read_number>=10:
			filter_set.add(iso)

with open(sys.argv[2]) as bed:
	with open(sys.argv[3],'w') as outfile:
		for line in bed:
			line=line.rstrip().split('\t')
			if line[3] in filter_set:
				outfile.write('\t'.join(line)+'\n')
				
with open(sys.argv[2]) as bed:
	with open(sys.argv[3],'w') as outfile:
		for line in bed:
			line=line.rstrip().split('\t')
			if line[3] in filter_set:
				outfile.write('\t'.join(line)+'\n')

with open(sys.argv[4]) as fasta:
	with open(sys.argv[5],'w') as fa_out:
		while filter_set:
			idline = fasta.readline()
			seq = fasta.readline()
			gene=idline[1:idline.find('\n')]
			if gene in filter_set:
				fa_out.write('%s%s' % (idline,seq))
				filter_set.remove(gene)