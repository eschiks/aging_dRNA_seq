#!/bin/bash

basename='file_basename'

# pull primary alignments from nanopore bams
samtools view -b -F0x100 -F0x900 ${basename}.sorted.bam > ${basename}_primary.sorted.bam

# convert primary bam to bed12
bamToBed -bed12 -split -i ${basename}_primary.sorted.bam > ${basename}.bed

# change chromosome names to be compatible with Roach nanopore scripts
sed -i 's/MtDNA/M/g' ${basename}.bed 
sed -i 's/^/chr/' ${basename}.bed

# Roach et al. 2020 script to filter full length transcripts - I made some edits to this to be compatible with my genome annotation files (edited script in this directory)
TSS_filter.py ${basename}.bed ${basename}_tss_filtered.bed

# filter for reads with 'pass' polyA tails
polya_filter.py ${basename}_polya.tsv ${basename}_tss_filtered.bed ${basename}_tss_polya_filtered.bed

# filter fastq files for pass reads
fastq_filter.py ${basename}_tss_polya_filtered.bed ${basename}.fastq ${basename}_tss_polya.fastq