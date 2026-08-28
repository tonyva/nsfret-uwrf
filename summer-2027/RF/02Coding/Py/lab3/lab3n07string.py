#!/usr/bin/python3 -W all
#
# Python program showing a pitfall in using string replacement

dna = "AGTCGC"
swapped = dna.replace( 'G', 'C' )
swapped = dna.replace( 'C', 'G' )
print ( "1: replacing Gs with Cs and Cs with Gs:" )
print ( "   ", dna, "converted to", swapped )


swapped = dna.replace( 'C', 'G' )
swapped = dna.replace( 'G', 'C' )
print ( "2: replacing Cs with Gs and Gs with Cs:" )
print ( "   ", dna, "converted to", swapped )

swapped = dna.replace( 'C', 'G' )
swapped = swapped.replace( 'G', 'C' )
print ( "3: replacing Cs with Gs and Gs with Cs:" )
print ( "   ", dna, "converted to", swapped )
