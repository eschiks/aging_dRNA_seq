#!/bin/bash

basename='file_basename'

# set up directories
mkdir ./${basename} && cd ./${basename} && mkdir fastq

# move single fastq file into fastq directory
cp ${basename}.fastq ./fastq

# fasta must be in $basename directory (can't give absolute path to program) - copied it in
nanopsu alignment -i ./fastq -r c_elegans.PRJNA13758.WS279.genomic.fa

# need to remove anything that's not an output from the alignment step
rm -r ./fastq
rm c_elegans.PRJNA13758.WS279.genomic.fa

nanopsu remove_intron

nanopsu extract_features

nanopsu prediction

# this script pulls high confidence sites and gives a cleaner output
./clean_prediction_csv.py ./alignment/prediction.csv ${basename}_prediction.txt