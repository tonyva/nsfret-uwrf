#!/usr/bin/python3
#
# Python program showing how to slice and dice arrays
#
bases = [ 'A', 'C', 'G', 'T' ]
print ( "Here are the array elements: ", bases )
e = bases.pop( 0 )
bases.append( e )
print ( "Element from beginning put at the end: ", bases )
