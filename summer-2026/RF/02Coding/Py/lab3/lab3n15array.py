#!/usr/bin/python3 -W all
#
# Python program to convert a string to an array of characters
import re

dna = "ATCCTTTATAGGTATATC"
print ( "Original sequence:", dna )
dna_array = list( dna )
print ( dna_array )
for nuc in dna_array:
    print ( " : ", nuc )
