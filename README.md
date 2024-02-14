# GDC-Case-IDs

This script recovers Case IDs from a list of filenames from the Genomic Data Commons Data Portal Repository using GDC API

## Instructions

1. Copy the UUIDs and filenames from your GDC manifest file
   ![image](https://github.com/u-kapoor/GDC-Case-IDs/assets/160059835/df4d6980-2683-4d9a-82fb-28dcaa670d02)
2. Use VLOOKUP on excel to get sample UUIDs given the file name from the GDC manifest file that matches with VDJ recovered filename
   Filenames from the VDJ recoveries have the format "sliced_XXX.bam.tsv", so it may be helpful to convert to "XXX.bam" first, followed by a VLOOKUP to your manifest UUIDs/filenames
3. Copy the sample UUIDs to a blanck csv file
4. Update the filepath/filename on the script to point to this csv file and run
