#!/usr/bin/env python3

# make SUPPA compatible gtf file with collapsed isoforms from flair

import pybedtools

bed=pybedtools.BedTool('collapse_new_10p_filtered_named.isoforms.bed')
tmp=pybedtools.BedTool.bed12tobed6(bed)
pybedtools.BedTool.sort(tmp).saveas('tmp.bed')

with open('collapse_new_10p_filtered_named.isoforms.gtf','w') as gtf:
    with open('tmp.bed') as bed:
        for line in bed:
            line=line.strip().split()
            chrom,start,end,name,strand=line[0],line[1],line[2],line[3],line[5]
            source="flair"
            gene_id=name[name.rfind('_')+1:]
            tx_id=name
            description='gene_id "%s"; transcript_id "%s"' % (gene_id,tx_id)
            outline=[chrom,source,'exon',start,end,'.',strand,'.',description]
            gtf.write('\t'.join(outline)+'\n')