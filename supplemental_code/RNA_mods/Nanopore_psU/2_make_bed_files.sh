#!/bin/bash

# output from nanopsu has - strand sites indexed in reverse. Need to correct this. Also want sites that are present in all 3 reps for each day and get a mean confidence number and sum number of sites.

LINE=$(cat "daylist.txt")
for f in $LINE
do
./all_reps_sites.py ./${f}_rep1/${f}_rep1_prediction.txt ./${f}_rep2/${f}_rep2_prediction.txt ./${f}_rep3/${f}_rep3_prediction.txt c_elegans.PRJNA13758.WS279.chromSizes ${f}_consistent_sites.txt
done