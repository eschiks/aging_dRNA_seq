#!/bin/bash

# pull out all CDS sites from features files

grep 'CDS' young_all_reps_AG_FEATURES_final.bed | awk -v OFS='\t' '{print $1, $2, $3, $4, $5, $6}' > cds_edits_young.bed

grep 'CDS' old_all_reps_AG_FEATURES_final.bed | awk -v OFS='\t' '{print $1, $2, $3, $4, $5, $6}' > cds_edits_old.bed

# convert to sorted VCF format

./make_vcf.py cds_edits_young.bed young_cds_AG.vcf
./make_vcf.py cds_edits_old.bed old_cds_AG.vcf
cat young_cds_AG.vcf | awk '$1 ~ /^#/ {print $0;next} {print $0 | "sort -k1,1 -k2,2n"}' > young_cds_AG.sorted.vcf
cat old_cds_AG.vcf | awk '$1 ~ /^#/ {print $0;next} {print $0 | "sort -k1,1 -k2,2n"}' > old_cds_AG.sorted.vcf

# Use these files to run Variant Annotation Integrator from UCSC - parameters file is in this directory!
