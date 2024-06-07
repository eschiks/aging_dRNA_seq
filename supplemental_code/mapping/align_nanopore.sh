#!/bin/bash

# combine fastq files for live basecalling

cat *.fastq > dayx_repx.fastq

# minimap2 map Nanopore reads

for f in *.fastq
do
minimap2 -a -x splice -uf -k14 c_elegans.PRJNA13758.WS279.genomic.fa $f > ${f}.aligned.sam
done

# sam to bam

for f in *.sam
do samtools view -S -b $f > ${f%.*}.bam
done

# sort bam

for g in *.bam
do samtools sort $g -o ${g%.*}.sorted.bam
done

# index bam

for h in *.sorted.bam
do samtools index $h
done