#!/bin/bash

# index fast5 files and call polyA tails

for f in *.fastq
do
basename=${f%.*}
nanopolish index -d ${basename}/fast5_pass/ ${basename}.fastq
nanopolish polya --threads=24 --reads=${basename}.fastq --bam=${basename}.sorted.bam --genome=c_elegans.PRJNA13758.WS279.genomic.fa > ${basename}_polya.tsv
done
