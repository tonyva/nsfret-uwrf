#!/usr/bin/python3
#
# Python program to get input from a file into a list or array
#
infilename = "numbers.txt"
inpf = open( infilename, "r" )
listofnumbers = []
s = inpf.readline()
while ( s != '' ):
    listofnumbers.append( int(s) )
    s = inpf.readline()
inpf.close()

print ( "List read from ", infilename, " is:", listofnumbers )
