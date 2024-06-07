#!/usr/bin/env python3

# inputs: 1=bed file with filtered reads, 2=unfiltered fastq file, 3=output fastq file

# code for parsing fastq derived from seqtk - https://github.com/lh3/seqtk

import sys
filter_set=set()

# pull reads that pass polya and TSS filters

with open(sys.argv[1]) as filtered:
	for line in filtered:
		line=line.rstrip().split()
		filter_set.add(line[3])

# parse fastq file and extract reads in polya_set

outfile=open(sys.argv[3],'w') 

with open(sys.argv[2],"r") as fastq:
	while filter_set:
		idline = fastq.readline()
		seq = fastq.readline()
		spacer = fastq.readline()
		quals = fastq.readline()
		if idline.split(' ')[0].split('@')[1] in filter_set:
			outfile.write('%s%s%s%s%%' % (idline,seq,spacer,quals))
			filter_set.remove(idline.split(' ')[0].split('@')[1])