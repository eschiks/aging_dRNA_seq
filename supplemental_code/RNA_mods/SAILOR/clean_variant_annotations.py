#!/usr/bin/env python3

# take the files output from Variant Annotation Integrator and get them in a usable format

# the main thing here is that this tool is designed for SNP calling, so it doesn't take strand into account. Therefore, we want to get rid of SNPs that are on the opposite strand as our mutations. 

import sys

def find_gene_id(x):
    start = x.index('gene_id') + len('gene_id')+2
    start_to_end = x[start:]
    end = start_to_end.index(';')-1
    return start_to_end[:end]

# pull strand info from gtf

strand_dict={}
with open('c_elegans.PRJNA13758.WS279.canonical_geneset.gtf') as gtf:
    for line in gtf:
        if line.startswith('#'):
            pass
        else:
            line=line.strip().split('\t')
            if 'gene_id' in line[8]:
                wb,strand=find_gene_id(line[8]),line[6]
                if wb not in strand_dict:
                    strand_dict[wb]=strand
    
with open(sys.argv[1]) as variants:
    with open(sys.argv[2],'w') as outfile:
        for line in variants:
            if line.startswith('Uploaded'):
                pass
            else:
                fields=line.strip().split()
                strand=fields[0].split(':')[3]
                gene=fields[3].replace('Gene:','') # a few gene names have 'Gene:' before them
                if gene in strand_dict:
                    if strand_dict[gene]==strand:
                        if strand=='-' and fields[2]=='C':# if the gene strand matches the site strand
                            outfile.write(line)
                        elif strand=='+' and fields[2]=='G':
                            outfile.write(line)