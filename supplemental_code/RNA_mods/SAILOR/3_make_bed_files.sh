#!/bin/bash

# get sites present in all 3 replicates

LINE=$(cat "daylist.txt")
for f in $LINE
do
./all_reps_sites.py ${f}_rep1_AG_edits_filtered.bed ${f}_rep2_AG_edits_filtered.bed ${f}_rep3_AG_edits_filtered.bed ${f}_all_reps_AG_filtered.bed
done