#!/usr/bin/python3 -W all
#
# Python program with string input and matching
#
userinput = input( "  Please enter a string: ")

if ( userinput.find( 'abcd' ) >= 0 ) :
    print ( "  your string contained the pattern 'abcd'!" )
else:
    print ( "  your string did not have an 'abcd' in it" )
