#!/usr/bin/python3 -W all
#
# Python program with regular expressions
import re

seq = "ATCCTTTATAGGC"
motif = '(TA){2}'

print ( "Search using regular expression for TATA:" )
if ( re.search( motif, seq )):
    print ( "  seq ", seq, " contains the substring 'TATA'" )
else:
    print ( "  seq ", seq, " does not contain the substring 'TATA'" )
