#!/bin/bash

snakemake --snakefile ~/FLARE/workflow_sailor/Snakefile --configfile sailor.json --verbose --use-singularity --singularity-args '--bind ~/ --bind ./bams --bind ./outputs --bind ./genome_files' -j1