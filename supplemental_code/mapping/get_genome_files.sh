#!/bin/bash

#gff3
wget https://downloads.wormbase.org/releases/WS279/species/c_elegans/PRJNA13758/c_elegans.PRJNA13758.WS279.annotations.gff3.gz && gunzip c_elegans.PRJNA13758.WS279.annotations.gff3.g

#gtf
wget https://downloads.wormbase.org/releases/WS279/species/c_elegans/PRJNA13758/c_elegans.PRJNA13758.WS279.canonical_geneset.gtf.gz && gunzip c_elegans.PRJNA13758.WS279.canonical_geneset.gtf.gz

#reference genome
wget https://downloads.wormbase.org/releases/WS279/species/c_elegans/PRJNA13758/c_elegans.PRJNA13758.WS279.genomic.fa.gz && gunzip c_elegans.PRJNA13758.WS279.genomic.fa.gz

#make reference transcriptome
gffread -F -w c_elegans.PRJNA13758.WS279.transcriptome.fa -g c_elegans.PRJNA13758.WS279.genomic.fa c_elegans.PRJNA13758.WS279.canonical_geneset.sorted.gtf

#make chromosome sizes file
faidx c_elegans.PRJNA13758.WS279.genomic.fa -i chromsizes > c_elegans.PRJNA13758.WS279.chromSizes