#!/usr/bin/python3 -W all
#
# Python program showing how to use string replacement

dna = "ATTTCAGCATTG"
rna = dna.replace( 'T', 'U' )
print ( "1: Simple use of replace function:" )
print ( "   ", dna, "converted to", rna )


second = dna.replace( 'T', 'U', 3 )
print ( "2: replace function for first 3 occurences:" )
print ( "   ", dna, "converted to", second )
