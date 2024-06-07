#!/bin/bash

# combine filtered fastq files from all reps
cat *_tss_polya.fastq > all_reps_tss_polya.fastq

# combine corrected bed files from all reps
cat *all_corrected.bed > all_corrected.bed

# run flair collapse
python flair.py collapse --isoformtss --annotation_reliant generate --check_splice --support 0.10 -t 16 -g c_elegans.PRJNA13758.WS279.genomic.fa -f c_elegans.PRJNA13758.WS279.canonical_geneset.gtf -r all_reps_tss_polya.fastq -q all_corrected.bed --temp_dir ./tmp --generate_map -o collapse_10p

# remove isoforms with <10 supporting reads
filter_isoforms_by_reads.py collapse_10p.combined.isoform.read.map.txt collapse_10p.isoforms.bed collapse_new_10p_filtered.isoforms.bed collapse_10p.isoforms.fa collapse_10p_filtered.isoforms.fa