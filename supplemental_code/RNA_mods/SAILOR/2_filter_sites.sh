#!/bin/bash

# filter outputs - require ≥5% of gene to be edited, ≥20 reads, ≥75% confidence score

LINE=$(cat "replist.txt")
for f in $LINE
do
./filter_sites.py ${f}_AG_edits.bed 
done
