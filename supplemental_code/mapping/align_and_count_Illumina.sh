#!/bin/bash

# generate genome
STAR --runThreadN 16 --genomeSAindexNbases 12 --runMode genomeGenerate --genomeDir ./ce11_WS279_genome_index --genomeFastaFiles c_elegans.PRJNA13758.WS279.genomic.fa --sjdbGTFfile c_elegans.PRJNA13758.WS279.annotations.gff3 

# STAR mapping for gene expression analyses
for f in *_R1.fastq.gz
do
DBDIR=ce11_WS279_genome_index
basename=${f%_R1*}
read1=$f
read2=${f%_R1.fastq.gz}_R2.fastq.gz
STAR --runThreadN 24 --readFilesCommand zcat --genomeDir $DBDIR --readFilesIn $read1 $read2 --outSAMtype BAM SortedByCoordinate --outFileNamePrefix ./alignments/$basename
done

# index bam files

for j in ./alignments/*.bam
do samtools index $j
done

# feature counts

featureCounts *.bam -p -s 2 -a c_elegans.PRJNA13758.WS279.canonical_geneset.gtf -o all_days_WS279_featurecounts.txt