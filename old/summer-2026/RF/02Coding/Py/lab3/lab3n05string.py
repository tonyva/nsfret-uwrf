#!/usr/bin/python3 -W all
#
# Python program with string input and matching

seq = "ATCCTTTGGC"


print ( "1: Using the 'in' operator :" )
if ( 'TTC' in seq or 'TTT' in seq ):
    print ( "  seq ", seq, " contains the substring 'TTC' or 'TTT'" )
else:
    print ( "  seq ", seq, " does not contain the substring 'TTC' or 'TTT'" )

import re                 # import regular expression library of functions

print ( "2: Using regular expression TTC|TTT :" )
regs = 'TTC|TTT' 
if ( re.search( regs, seq )):
    print ( "  seq ", seq, " contains the substring 'TTC' or 'TTT'" )
else:
    print ( "  seq ", seq, " does not contain the substring 'TTC' or 'TTT'" )


print ( "3: Using regular expression TTT|TTC :" )
regs = 'TTT|TTC' 
if ( re.search( regs, seq )):
    print ( "  seq ", seq, " contains the substring 'TTC' or 'TTT'" )
else:
    print ( "  seq ", seq, " does not contain the substring 'TTC' or 'TTT'" )


print ( "4: Using regular expression TT[TC] :" )
regs = 'TT[TC]' 
if ( re.search( regs, seq )):
    print ( "  seq ", seq, " contains the substring 'TTC' or 'TTT'" )
else:
    print ( "  seq ", seq, " does not contain the substring 'TTC' or 'TTT'" )
