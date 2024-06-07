#!/usr/bin/env python3

# take bedfa of UTRs and searches for Mangone et al. motifs in the last 50 nts
import sys,os,pybedtools

bed=open(sys.argv[1],'r')
utr=pybedtools.BedTool(bed)
genome = pybedtools.example_filename(sys.argv[2]) # genome fasta file
utr_fa = utr.sequence(fi=genome,name=True,s=True,split=True)
utr_fa.save_seqs('tmp.fa')
bed.close()

distance_dict={}
motif_dict={}
motif_list=[]

with open(sys.argv[3],'r') as motif:
    for row in motif:
        row=row.strip()
        PAS=row.replace("U", "T" )
        motif_list.append(PAS)
    
with open('tmp.fa','r') as utrs:
    while True:
        readname=utrs.readline().strip().strip('>')
        seq=utrs.readline().strip()
        gene=readname[:readname.find('::')]
        if productive in gene:
            if len(seq)<50:
                last_50=seq
            else:
                last_50=seq[-50:]
            for PAS in motif_list:
                if gene in motif_dict:
                    break
                if PAS in last_50:
                    motif_dict[gene]=PAS
                    dist_from_end=len(seq[seq.rfind(PAS):])
                    distance_dict[gene]=dist_from_end	
                if PAS not in last_50:
                    continue
            if gene not in motif_dict:
                motif_dict[gene]="no PAS"
                distance_dict[gene]="NA"
            if not seq:
                break

os.remove('tmp.fa')
outfile=open(sys.argv[4],'w')
outfile.write('isoform' + '\t' + 'motif' + '\t' + 'distance_from_three_prime_end' + '\n')

for gene in motif_dict:
    motif=motif_dict[gene]
    distance=str(distance_dict[gene])
    outfile.write(gene + '\t' + motif + '\t' + distance +'\n')		
