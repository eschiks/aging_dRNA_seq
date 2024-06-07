#!/bin/bash

basename='file_basename'

# used flair v. 1.7

# flair script to pull Illumina splice junctions 
junctions_from_sam.py -s ${basename}_Illumina.sorted.bam -n $basename

# flair correct splice junctions
python flair.py correct -t 16 -o $basename -q ${basename}.bed -g c_elegans.PRJNA13758.WS279.genomic.fa -c c_elegans.PRJNA13758.WS279.chromSizes -j ${basename}_junctions_filtered.bed -f c_elegans.PRJNA13758.WS279.canonical_geneset.gtf