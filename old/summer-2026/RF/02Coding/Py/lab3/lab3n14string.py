#!/usr/bin/python3 -W all
#
# Python program with regular expressions
import re

dna = "ATCCTTTATAGGTATATC"
motif1 = re.compile( '(TA){2}' )
motif2 = 'TAAT'

newseq = motif1.sub( motif2, dna )
print ( "Original sequence: ", dna )
print ( "After substitution:", newseq )
