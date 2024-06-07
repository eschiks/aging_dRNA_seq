#!/usr/bin/env python3

import pandas as pd

counts=pd.read_csv('flair.quantify.counts_named.tsv', sep='\t')

day2= counts[["ids", "day1rep1_day1_batch1","day1rep2_day1_batch1","day1rep3_day1_batch1","day2rep1_day2_batch1","day2rep2_day2_batch1","day2rep3_day2_batch1"]]
day2.to_csv("day1_day2_counts_final.tsv",sep='\t',index=False)
day3= counts[["ids", "day1rep1_day1_batch1","day1rep2_day1_batch1","day1rep3_day1_batch1","day3rep1_day3_batch1","day3rep2_day3_batch1","day3rep3_day3_batch1"]]
day3.to_csv("day1_day3_counts_final.tsv",sep='\t',index=False)
day4= counts[["ids", "day1rep1_day1_batch1","day1rep2_day1_batch1","day1rep3_day1_batch1","day4rep1_day4_batch1","day4rep2_day4_batch1","day4rep3_day4_batch1"]]
day4.to_csv("day1_day4_counts_final.tsv",sep='\t',index=False)
day5= counts[["ids", "day1rep1_day1_batch1","day1rep2_day1_batch1","day1rep3_day1_batch1","day5rep1_day5_batch1","day5rep2_day5_batch1","day5rep3_day5_batch1"]]
day5.to_csv("day1_day5_counts_final.tsv",sep='\t',index=False)
day7= counts[["ids", "day1rep1_day1_batch1","day1rep2_day1_batch1","day1rep3_day1_batch1","day7rep1_day7_batch1","day7rep2_day7_batch1","day7rep3_day7_batch1"]]
day7.to_csv("day1_day7_counts_final.tsv",sep='\t',index=False)
day10= counts[["ids", "day1rep1_day1_batch1","day1rep2_day1_batch1","day1rep3_day1_batch1","day10rep1_day10_batch1","day10rep2_day10_batch1","day10rep3_day10_batch1"]]
day10.to_csv("day1_day10_counts_final.tsv",sep='\t',index=False)
day15= counts[["ids", "day1rep1_day1_batch1","day1rep2_day1_batch1","day1rep3_day1_batch1","day15rep1_day15_batch1","day15rep2_day15_batch1","day15rep3_day15_batch1"]]
day15.to_csv("day1_day15_counts_final.tsv",sep='\t',index=False)