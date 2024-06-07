#!/bin/bash

./make_tables_for_diff_exp.py

LINE=$(cat "daylist.txt")
for f in $LINE
do
python flair.py diffExp --out_dir_force --exp_thresh 5 -q counts_matrix_day1_${f}.tsv -t 8 -o ${f}_out
python flair.py diffSplice --test -i collapse_new_10p_filtered_named.isoforms.bed -q counts_matrix_day1_${f}.tsv -t 8 -o ${f}_diff_splice_out
done