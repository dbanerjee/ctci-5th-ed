# Solution to Exercise 11.4 from Cracking the Coding Interview, 5th Edition
# Nitin Punjabi
# nptoronto@yahoo.com
# https://github.com/nitinpunjabi

# Steps
# (1) Determine how much of the file I can load and manipulate in memory. This
# amount is designated as N.
#
# (2) Read the file into memory N chunks at a time. Sort each chunk in-memory
# using a conventional sorting routine.
#
# (3) Output the sorted chunk into its own file. Processing the 20Gb file in
# this manner should lead to N files of sorted data.
# 
# (4) Using the merge step from mergesort, read in the sorted files in parallel,
# merging the contents and outputting the merged stream into a single file.
# Alternatively, if the number of files is huge, use map/reduce to merge sets of
# files simultaneously into intermediate files, building up to the sorted file.
