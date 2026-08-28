#!/usr/bin/python3 -W all
#
# Python program showing how to use translation tables

dna = "AGTCGC"
table = dna.maketrans( 'GC', 'CG' )
swapped = dna.translate( table )
print ( "Replacing Gs with Cs and Cs with Gs:" )
print ( "   ", dna, "converted to", swapped )
