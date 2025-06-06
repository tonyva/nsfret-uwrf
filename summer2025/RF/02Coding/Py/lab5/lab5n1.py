#!/usr/bin/python3
dnaseq = "GATCGCacgtcAGC"
print ( "Starting DNA sequence is: ", dnaseq )

dna_array = list( dnaseq )

a_count = 0
c_count = 0
t_count = 0
g_count = 0

for nuc in dna_array:
   if ( nuc == 'A' ):
      a_count += 1
   elif ( nuc == 'C' ):
      c_count += 1
   elif ( nuc == 'T' ):
      t_count += 1
   else:
      g_count += 1
#
#  print counts of A, C, T and G
#
print ( " Counts:" )
print ( "   A: ", a_count )
print ( "   C: ", c_count )
print ( "   T: ", t_count )
print ( "   G: ", g_count )

