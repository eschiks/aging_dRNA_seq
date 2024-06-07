#!/bin/bash

# get features that overlap with psU sites

# make files with genome features to intersect with psU site beds
./make_genome_features_beds.py

# introns.bed came from pull_unique_introns.py script in ~/Illumina_splicing/intron_mapping
cat genome_exons_no_utr_no_SC.bed genome_start_stop.bed genome_utrs.bed introns.bed > genome_features.bed

basename='file_basename'

# convert consistent sites file to bed file
./make_beds.py ${basename}_consistent_sites.txt ${basename}_consistent_sites.bed

# intersect psU sites with feature files
bedtools intersect -s -wo -a genome_features.bed -b ${basename}_consistent_sites.bed > ${basename}_psU_features.bed
bedtools intersect -s -wo -a genome_biotype.bed -b ${basename}_consistent_sites.bed > ${basename}_psU_biotype.bed