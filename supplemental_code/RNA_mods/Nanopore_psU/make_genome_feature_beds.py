#!/usr/bin/env python3

def get_gene_biotype(string):
    sub=string[(string.find('gene_biotype')+len('gene_biotype')+2):]
    return sub[:sub.find('"')]

# bed with coordinates and biotypes
with open('c_elegans.PRJNA13758.WS279.canonical_geneset.sorted.gtf') as gtf:
    with open('genome_biotype.bed','w') as outfile:
        for line in gtf:
            line=line.strip().split('\t')
            if line[2]=='gene':
                chrom,start,end,score,strand=line[0],line[3],line[4],'60',line[6]
                name=get_gene_biotype(line[8])
                out=[chrom,start,end,name,score,strand]
                outfile.write('\t'.join(out)+'\n')

# bed with annotated UTRs                
with open('c_elegans.PRJNA13758.WS279.canonical_geneset.sorted.gtf') as gtf:
    with open('genome_utrs.bed','w') as outfile:
        for line in gtf:
            line=line.strip().split('\t')
            if 'utr' in line[2]:
                name=line[2]
                chrom,start,end,score,strand=line[0],line[3],line[4],'60',line[6]
                out=[chrom,start,end,name,score,strand]
                outfile.write('\t'.join(out)+'\n')
                
# bed with exon features
with open('c_elegans.PRJNA13758.WS279.canonical_geneset.sorted.gtf') as gtf:
    with open('genome_exons.bed','w') as outfile:
        for line in gtf:
            line=line.strip().split('\t')
            if line[2]=='exon':
                name=line[2]
                chrom,start,end,score,strand=line[0],line[3],line[4],'60',line[6]
                out=[chrom,start,end,name,score,strand]
                outfile.write('\t'.join(out)+'\n')
                
# remove utr sequences from exon bed
import pybedtools
a=pybedtools.BedTool('genome_exons.bed')
b=pybedtools.BedTool('genome_utrs.bed')
a.subtract(b,s=True).saveas('genome_exons_no_utr.bed')

# make start and stop codon bed
with open('c_elegans.PRJNA13758.WS279.canonical_geneset.sorted.gtf') as gtf:
    with open('genome_start_stop.bed','w') as outfile:
        for line in gtf:
            line=line.strip().split('\t')
            if 'codon' in line[2]:
                name=line[2]
                chrom,start,end,score,strand=line[0],line[3],line[4],'60',line[6]
                out=[chrom,start,end,name,score,strand]
                outfile.write('\t'.join(out)+'\n')
                
a=pybedtools.BedTool('genome_exons_no_utr.bed')
b=pybedtools.BedTool('genome_start_stop.bed')

a.subtract(b,s=True).saveas('genome_exons_no_utr_no_SC.bed') # this file only has exon sequences that don't overlap with UTR or start/stop codon features