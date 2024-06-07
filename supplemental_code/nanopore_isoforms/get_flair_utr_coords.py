#!/usr/bin/env python3

# pulls 3'UTR coordinates for productive isoforms from FLAIR collapse

import sys

productivity = open('isoform_productivity_new_named.bed','r') 
#bed6 = open('test.bed','r') # sorted
bed6 = open('collapse_10p_filtered_named.isoforms.sorted.bed6','r') # sorted
utr = open('flair_10p_filtered_utrs.bed6','w') 

utr_start_dict = {}
for line in productivity:
	fields = line.strip().split()
	if fields[-1] == "PRO":
		if fields[5] == '+':
			utr_start_dict[fields[3]] = int(fields[7])
		if fields[5] == '-':
			utr_start_dict[fields[3]] = int(fields[6])
productivity.close()

for line in bed6:
	fields = line.strip().split()
	name=fields[3]
	strand=fields[5]
	start=str(int(fields[1])) # correct issue with bed6 to bed12 conversion where start coords are off by 1
	fields[1]=start 
	end=fields[2]
	if name in utr_start_dict:
		utr_start=utr_start_dict[name]
		if strand == "+":
			if int(end)<utr_start and int(start)<utr_start: # if exon doesn't contain any 3'UTR sequence
				pass
			if int(start)<utr_start and int(end)>=utr_start:
				if int(end)==utr_start: # make sure end and start coords are not equal
					continue
				else:
					start=str(utr_start)
					fields[1]=start
				utr.write("\t".join(fields)+'\n')
				continue
			elif int(start)>=utr_start and int(end)>utr_start:
				utr.write("\t".join(fields)+'\n') 
		if strand == "-":
			if int(end)<=utr_start and int(start)<utr_start: # if exon doesn't contain any 3'UTR sequence
				utr.write("\t".join(fields)+'\n')
				continue
			if int(start)>utr_start and int(end)>utr_start:
				pass
			if int(start)<=utr_start and int(end)>utr_start:
				if int(start)==utr_start: # make sure end and start coords are not equal
					continue
				else:
					end=str(utr_start)
					fields[2]=end
				utr.write("\t".join(fields)+'\n')
bed6.close()
utr.close()
