#!/usr/bin/python3

#------------------------
# Our functions:
# 1. lookfor - looks for a single character in a string at a
#              particular position and returns:
#                  either 0 (not found) or 1 (found).
# 2. countLetter - counts the number of occurrences of a letter
#              within a string and returns:
#              a 0 or a positive number.
#------------------------
def lookfor(c, seq, i):
    nuc = seq[i]
    if ( nuc == c ):
      return 1
    return 0

def countLetter( c, seq ):  # <---parameters
#----local variables
    count = 0;

    for aa in seq:
        if aa == c:
            count += 1
#----output or return value
    return count

dnaseq = "GATCGCacgtcAGC"
print ( "Starting DNA sequence is: ", dnaseq )
print ( "   Length of sequence is: ", len(dnaseq) )

#
#  print counts of A, C, T and G
#
print ( " Counts: " )
print ( "   A: ", countLetter( 'A',  dnaseq ) )
print ( "   C: ", countLetter( 'C',  dnaseq ) )
print ( "   T: ", countLetter( 'T',  dnaseq ) )
print ( "   G: ", countLetter( 'G',  dnaseq ) )

