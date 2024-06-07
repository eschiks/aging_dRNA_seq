#!/usr/bin/env python3

import sys

day=str(sys.argv[1])

unpro_counts=0
pro_counts=0
total=0

if day=='all':
	with open(sys.argv[2], 'r') as counts_file:
		for line in counts_file:
			line=line.rstrip().split('\t')
			if 'unproductive' in line[0]: # unproductive novel isos 
				total+=1
				unpro_counts+=1
			elif 'productive' in line[0]: # productive novel isos exp
				total+=1
				pro_counts+=1
			elif 'productive' not in line[0]: # all isos exp
				total+=1
else:
	with open(sys.argv[2], 'r') as counts_file:
		for line in counts_file:
			line=line.rstrip().split('\t')
			if line[0]=='ids': # skip first line
				continue
			if day=='day1': # pull counts from first 3 columns
				counts=float(line[1])+float(line[2])+float(line[3])
			else:
				counts=float(line[4])+float(line[5])+float(line[6])
			if 'unproductive' in line[0] and counts>0: # unproductive novel isos exp at this day
				total+=1
				unpro_counts+=1
			elif 'productive' in line[0] and counts>0: # productive novel isos exp at this day
				total+=1
				pro_counts+=1
			elif 'productive' not in line[0] and counts>0: # all isos exp at this day
				total+=1

print(day+'\t'+str(total)+'\t'+str(pro_counts)+'\t'+str(unpro_counts))