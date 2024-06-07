#!/bin/bash

# get unique intron coordinates based on gtf file
./pull_unique_introns.py c_elegans.PRJNA13758.WS279.canonical_geneset.gtf introns.bed introns.saf

# featureCounts to assign reads to introns - Illumina read alignments
featureCounts *.bam -s 2 --fracOverlap 0.5 -p -T 8 -F SAF -a introns.saf -o introns_fc.txt