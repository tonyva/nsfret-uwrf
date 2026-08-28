#!/usr/bin/python3

#------------------------
# Our function:
# lookfor - looks for a single character in a string at
#    a particular position and returns
#           either 0 (not found) or 1 (found).
#------------------------
def lookfor( c, seq, i ):
    nuc = seq[i]
    if ( nuc == c ):
        return 1
    return 0
#------------------------

dnaseq = "GATCGCacgtcAGC"
print ( "Starting DNA sequence is: ", dnaseq )

a_count = 0
c_count = 0
t_count = 0
g_count = 0

for index in range( len(dnaseq)):
    a_count += lookfor( 'A' , dnaseq, index )
    c_count += lookfor( 'C' , dnaseq, index )
    t_count += lookfor( 'T' , dnaseq, index )
    g_count += lookfor( 'G' , dnaseq, index )
#
#  print counts of A, C, T and G
#
print ( " Counts:" )
print ( "   A: ", a_count )
print ( "   C: ", c_count )
print ( "   T: ", t_count )
print ( "   G: ", g_count )
