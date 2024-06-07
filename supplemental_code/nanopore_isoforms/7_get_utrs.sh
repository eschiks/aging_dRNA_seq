#!/bin/bash

bed12ToBed6 -i collapse_new_10p_filtered_named.isoforms.bed > collapse_new_10p_filtered_named.isoforms.bed6

bedtools sort -i collapse_new_10p_filtered_named.isoforms.bed6 > collapse_new_10p_filtered_named.isoforms.sorted.bed6

# use productivity info to get coordinates of 3'UTRs in bed6 format
./get_flair_utr_coords.py
bedtools sort -i flair_10p_filtered_utrs.bed6 > flair_10p_filtered_utrs.bed6

# compare 3'UTRs to Wormbase annotations
./find_novel_utrs.py

# convert bed6 UTR file to bed12 format
./bed6_to_bed12.py flair_10p_filtered_utrs.sorted.bed6 flair_10p_filtered_utrs.sorted.bed12

# count number of novel and annotated 3'UTRs
echo -e 'day' '\t' 'total' '\t' 'annotated' '\t' 'novel' >> utr_counts.txt
./count_utrs.py all flair.quantify.counts_named.tsv >> utr_counts.txt # all days counts 
./count_utrs.py day1 counts_matrix_day1_day2.tsv >> utr_counts.txt # day 1 counts - done separately because day 1 is in all the counts files
LINE=$(cat "daylist.txt")
for f in $LINE
do
./count_utrs.py $f counts_matrix_day1_${f}.tsv >> utr_counts.txt
done

# get PAS motifs - compare to Mangone et al. top PAS motifs (requires pybedtools)
./get_PAS_motifs.py flair_10p_filtered_utrs.sorted.bed12 c_elegans.PRJNA13758.WS279.genomic.fa Mangone_top_PAS.txt mangone_pas_isoforms.txt

# get lengths of all 3'UTRs and novel 3'UTRs
./feature_lengths.py flair_10p_filtered_utrs.sorted.bed12 utr_lengths.txt
./novel_utr_lengths.py