#!/bin/bash

./get_all_utr_7mer_mirna_coords.py c_elegans.PRJNA13758.WS279.canonical_geneset.sorted.gtf c_elegans.PRJNA13758.WS279.genomic.fa target_scan_7mer_seeds.txt miR_site_7mer_coords.bed 

./get_all_utr_6mer_mirna_coords.py c_elegans.PRJNA13758.WS279.canonical_geneset.sorted.gtf c_elegans.PRJNA13758.WS279.genomic.fa target_scan_7mer_seeds.txt miR_site_6mer_coords.bed 

bedtools intersect -a young_all_reps_AG_filtered.bed -b miR_site_6mer_coords.bed -u -s | sort -t 't' -k1,1 -k2,2 > young_AG_miR_6mer_overlaps.bed

bedtools intersect -a old_all_reps_AG_filtered.bed -b miR_site_6mer_coords.bed -u -s | sort -t 't' -k1,1 -k2,2 > old_AG_miR_6mer_overlaps.bed

bedtools intersect -a young_all_reps_AG_filtered.bed -b miR_site_7mer_coords.bed -u -s | sort -t 't' -k1,1 -k2,2 > young_AG_miR_6mer_overlaps.bed

bedtools intersect -a old_all_reps_AG_filtered.bed -b miR_site_7mer_coords.bed -u -s | sort -t 't' -k1,1 -k2,2 > old_AG_miR_6mer_overlaps.bed