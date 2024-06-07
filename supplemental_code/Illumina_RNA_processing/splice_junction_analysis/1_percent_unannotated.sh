#!/bin/bash

# get percent unannotated junctions from SJ.out.tab files output by STAR mapping

for f in *SJ.out.tab
do
echo ${f%SJ*} >> unannotated_junction_percents.txt # print file identifier
./percent_unannotated_junctions.py c_elegans.PRJNA13758.WS279.canonical_geneset.gtf $f >> unannotated_junction_percents.txt # prints out % unannotated junction reads
done