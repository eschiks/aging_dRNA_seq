#!/bin/bash

basename='file_basename'

# run diffSplice for each individual replicate compared to day 1 to examine splicing event changes
suppa.py diffSplice --save_tpm_events -m empirical -gc -i flair_iso.events.ioe -p day1_events.psi ${basename}_events.psi -e day1_iso_counts.txt ${basename}_iso_counts.txt -o ${basename}_diffSplice