#!/usr/bin/python3
#
#
import re

dna = "GATCGCAGC"
print ( "Part 1: Starting DNA sequence is: ", dna )

inp = 'ATCG'
out = 'TAGC'
ttable = inp.maketrans( inp, out )
swapped = dna.translate( ttable )
print ( "        Ending DNA sequence is:   ", swapped, "\n\n" )

dnaseq = swapped;
print ( "Part 2: Starting with DNA sequence:         ", dnaseq )
rinp = 'ATCG'
rout = 'UAGC'
rtable = dnaseq.maketrans( rinp, rout )

rseq = dnaseq.translate( rtable )
rseq = ''.join( reversed( rseq ) )
print ( "        Reverse-complement RNA sequence is: ", rseq, "\n\n" )


print ( "Part 3: Starting with RNA sequence: ", rseq )
rna = rseq
threonines = 'AC[UCAG]'
if ( re.search( threonines, rna ) ):
   print ( "One or more threonines found in sequence" )
else:
   print ( "No Threonines in this sequence" )


