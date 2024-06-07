#!/bin/bash

predictProductivity -i collapse_10p_filtered.isoforms.bed -g c_elegans.PRJNA13758.WS279.canonical_geneset.gtf -f c_elegans.PRJNA13758.WS279.genomic.fa --append_column --longestORF > isoform_productivity_new.bed

./name_novel_isoforms_by_productivity.py

# count novel isoforms by day
echo -e 'day' '\t' 'total' '\t' 'unproductive' '\t' 'productive' >> iso_counts.txt
./count_novel_isoforms.py all flair.quantify.counts_named.tsv >> iso_counts.txt # all days counts 
./count_novel_isoforms.py day1 counts_matrix_day1_day2.tsv >> iso_counts.txt # day 1 counts
LINE=$(cat "daylist.txt")
for f in $LINE 
do
./count_novel_isoforms.py $f counts_matrix_day1_${f}.tsv >> iso_counts.txt
done

# count isoforms per gene
./isos_per_gene.py all flair.quantify.counts_named.tsv >> isos_per_gene.txt # all days counts 
./isos_per_gene.py day1 counts_matrix_day1_day2.tsv >> isos_per_gene.txt # day 1 counts
LINE=$(cat "daylist.txt")
for f in $LINE
do
./isos_per_gene.py $f counts_matrix_day1_${f}.tsv >> isos_per_gene.txt
done