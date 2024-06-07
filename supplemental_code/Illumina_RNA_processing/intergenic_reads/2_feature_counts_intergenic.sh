#!/bin/bash

featureCounts *.bam -s 2 --fracOverlap 0.5 -p -T 8 -F SAF -a ${genome_dir}/intergenic_regions.saf -o intergenic_fc.txt
