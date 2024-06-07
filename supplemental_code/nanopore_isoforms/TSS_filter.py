#!/usr/bin/env python2

# some minor edits made to be compatible with specific GFF file I used - all mods commented in (ES)

import sys
import sets
# import matplotlib.pyplot as plt


def splitAttributes(attr):
    fields = attr.split(';')
    attr_dict = {}
    for field in fields:
        key,val = field.split('=')
        attr_dict[key] = val
    return attr_dict

def attemptToCorrectRead(bedfields,offset):
    chrom = bedfields[0]
    name = bedfields[3]
    score = bedfields[4]
    strand = bedfields[5]
    thickStart = bedfields[6]
    thickEnd = bedfields[7]
    rgb = bedfields[8]
    blockCount = bedfields[9]
    blockSizes = [int(x) for x in bedfields[10].split(',')]
    blockStarts = [int(x) for x in bedfields[11].split(',')]
    if strand == '+':
        start = int(fields[1])
        end = int(fields[2])
    elif strand == '-':
        start = int(fields[2])
        end = int(fields[1])
    else:
        print "something went wrong"
    if offset > 0:
        #Start with positive strand
        if strand == '+':
            start = start - offset
            if len(blockStarts) > 1:
                blockStarts = [blockStarts[0]] + [x + offset for x in blockStarts[1:]]
            blockSizes[0] = blockSizes[0] + offset
            if bedfields[1] == bedfields[6]:
                bedfields[6] = str(start)
            bedfields[1] = str(start)
            bedfields[10] = ','.join([str(x) for x in blockSizes])
            bedfields[11] = ','.join([str(x) for x in blockStarts])
        if strand == '-':
            start = start + offset
            # blockStarts[-1] = blockStarts[-1]  offset
            blockSizes[-1] = blockSizes[-1] + offset
            if bedfields[2] == bedfields[7]:
                bedfields[7] = str(start)
            bedfields[2] = str(start)
            bedfields[10] = ','.join([str(x) for x in blockSizes])
            bedfields[11] = ','.join([str(x) for x in blockStarts])
    elif offset < 0:
        if strand == '+':
            start = start - offset
            if len(blockStarts) > 1:
                blockStarts = [blockStarts[0]] + [x + offset for x in blockStarts[1:]]
            blockSizes[0] = blockSizes[0] + offset
            if blockSizes[0] <= 0:
                print "zero sized exon produced"
                return ""
            if bedfields[1] == bedfields[6]:
                bedfields[6] = str(start)
            bedfields[1] = str(start)
            bedfields[10] = ','.join([str(x) for x in blockSizes])
            bedfields[11] = ','.join([str(x) for x in blockStarts])
        if strand == '-':
            start = start + offset
            # blockStarts[-1] = blockStarts[-1]  offset
            blockSizes[-1] = blockSizes[-1] + offset
            if blockSizes[-1] <= 0:
                print "zero sized exon produced"
                return ""
            if bedfields[2] == bedfields[7]:
                bedfields[7] = str(start)
            bedfields[2] = str(start)
            bedfields[10] = ','.join([str(x) for x in blockSizes])
            bedfields[11] = ','.join([str(x) for x in blockStarts])
    return '\t'.join(bedfields) + "\n"


reference_in = open("/expanse/lustre/scratch/eschiksn/temp_project/IAN_MAPPING/genome_files/c_elegans.PRJNA13758.WS279.annotations.sorted.gff3") # added path to my sorted gff3 file with comment lines removed (sort -k1,1 -k4,4n -k5,5n)
in_file = open(sys.argv[1],'r')
out_file = open(sys.argv[2],'w')

##Construct dictionary of donors and acceptor pairs
donors = {} # chr,strand -> set of donors on that chr strand
acceptors = {} #chr,strand -> set of acceptors on that chr strand
tx_id_to_gene = {}
donor_genes = {} #chr,strand,pos -> gene_id
acceptor_genes = {} #chr,strand,pos -> gene_id
tx_dict = {}
ambiguous_donors = sets.Set() #chr,strand,pos for donors with more than one gene assignment
ambiguous_acceptors = sets.Set() #chr,strand,pos for acceptors with more than one gene assignment
single_exon_genes = {}
tx_id_to_exons = {}
window = 100

for line in reference_in: 
    fields = line.strip().split()
    chrom = fields[0]
    if chrom == "MtDNA":
        chrom = "chrM"
    else:
        chrom = "chr" + chrom
    start = int(fields[3]) - 1
    end =  int(fields[4])
    strand = fields[6]
    if fields[2] == "exon":
        tx_id = fields[8].split(':')[1]
        index = tx_id.find('.') + 1
        if tx_id in tx_id_to_exons:
            tx_id_to_exons[tx_id].append((chrom,strand,start,end))
        else:
            tx_id_to_exons[tx_id] = [(chrom,strand,start,end)]
    elif fields[2] == "gene":
        attr = splitAttributes(fields[8])
        if "Name" in attr:
            gene_id = attr["Name"]
            if "sequence_name" in attr:
                tx_id = attr["sequence_name"]
                tx_id_to_gene[tx_id] = gene_id
# remove lines that print out that something went wrong because many genes don't have transcript IDs in this format in my gff, so they just get discarded which is fine (ES)
            
cage_dict = {}
cage_bed_in = open("/expanse/lustre/scratch/eschiksn/temp_project/IAN_MAPPING/genome_files/cage_sage_combined.ce11_converted.WBcel235.bed",'r') # path to CAGE file downloaded from references scripts
for line in cage_bed_in:
    fields = line.strip().split()
    chrom = fields[0]
    start = fields[1]
    #print("start is:", start)
    end = fields[2]
    #print("end is:", end)
    strand = fields[5]
    if (chrom,strand) not in cage_dict:
        cage_dict[(chrom,strand)] = sets.Set() # every line has chrom and strand
    for x in range(int(start),int(end) + 1):
        cage_dict[(chrom,strand)].add(x)
        
start_site_dict = {}
for tx_id in tx_id_to_exons: ## WARNING: GFF3 file must be sorted for this approach to work
    if not '.' in tx_id: # some gene names slipped through that aren't transcript IDs, so don't grab these by removing IDs that don't have a '.' (ES)
        pass
    exons = tx_id_to_exons[tx_id]
    index = tx_id.find('.') + 1
    t_flag = True
    while True:
        try:
            if t_flag: # For some reason some genes have a t instead of a # immediately after the 1st '.' because this format sucks
                if tx_id[index] != 't': # Need to handle that, so this is my solution.
                    int(tx_id[index])
            else:
                int(tx_id[index])
            index += 1
            t_flag = False
        except:
            break
    tx_id2 = tx_id[:index]
    if tx_id2 in tx_id_to_gene: # some transcripts that turned up in the tx_id_to_exons do not have associated WB IDs-manually checked some and they are associated with genes whose names have been changed. Only pull genes that have WB IDs (ES)
        gene_id = tx_id_to_gene[tx_id2]
    if len(exons) > 1:
        chrom = exons[0][0]
        strand = exons[0][1]
        if strand == '+':
            start = exons[0][2]
        elif strand == '-':
            start = exons[-1][3]
    else: #Ideally we'd want a way to match single exon reads with single exon genes
        chrom,strand,start,end = exons[0]
        if strand == '-':
            tmp = start
            start = end
            end = tmp
    if (chrom,strand) not in start_site_dict:
        start_site_dict[(chrom,strand)] = sets.Set()
    start_site_dict[(chrom,strand)].add(start)

offsets = []
close1 = 0
close2 = 0
# close3 = 0
close4 = 0
# close5 = 0
total = 0
for line in in_file: # in_file is the corrected bed
    fields = line.strip().split()
    chrom = fields[0]
    strand = fields[5]
    if strand == '+':
        start = int(fields[1])
    elif strand == '-':
        start = int(fields[2])
    else:
        print "something went wrong with strand"
    if (chrom,strand) in start_site_dict:
        if strand == '+':
            closest = 101
            for i,x in enumerate(range(start - 100, start + 101)):
            # for i,x in enumerate(range(start-100,start)):
                if x in start_site_dict[(chrom,strand)]:
                    offset = i - 100
                    # offest = i
                    if abs(offset) < abs(closest):
                        closest = offset
        elif strand == '-':
            closest = 101
            for i,x in enumerate(range(start + 100,start - 101,-1)):
                if x in start_site_dict[(chrom,strand)]:
                    offset = i - 100
                    # offset = i
                    if abs(offset) < abs(closest):
                        closest = offset    
    offsets.append(-closest)
    if -15 <= closest <= 100: #Only output those reads that fall within 15 bp downstream of TSS, or 10 bp upstream of it, go with closest TSS regardless of upstream/downstream. 
        close1 +=1
        out_file.write(attemptToCorrectRead(fields,0))
        
    elif (chrom,strand) in cage_dict:
        if start in cage_dict[(chrom,strand)]:
            close2 += 1
            out_file.write(attemptToCorrectRead(fields,0))
    if (chrom,strand) in cage_dict:
        if start in cage_dict[(chrom,strand)]:
            close4 += 1
    total += 1

