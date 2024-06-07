#!/bin/bash

# make gtf file for SUPPA
./make_compatible_gtf.py

# generate splicing events file
suppa.py generateEvents -i collapse_new_10p_filtered_named.isoforms.gtf -o flair_isos.events -e SE SS MX RI FL -f ioe
#Put all the ioe events in the same file:
awk '
    FNR==1 && NR!=1 { while (/^<header>/) getline; }
    1 {print}
' *.ioe > flair_iso.events.ioe

# combine iso counts for all reps
./make_iso_counts.py

# get PSI per event file
suppa.py psiPerEvent -i flair_iso.events.ioe -e iso_counts_all_reps.txt -o all_days_events

