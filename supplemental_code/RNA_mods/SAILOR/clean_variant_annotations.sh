#!/bin/bash

# extract useful information from output variant annotation files from UCSC

./clean_variant_annotations.py ./final_beds/old_cds_AG_variant.txt ./final_beds/old_cds_variant_cleaned.txt
./clean_variant_annotations.py ./final_beds/young_cds_AG_variant.txt ./final_beds/young_cds_variant_cleaned.txt 
