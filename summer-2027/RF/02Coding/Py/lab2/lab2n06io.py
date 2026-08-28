#!/usr/bin/python3
#
# Python program to print to a file rather than the screen
#
filename = 'output.txt'          # name of output file
outf = open(  filename,  'w' )   # open the file for "w"riting

count = 0
while (count < 10 ):
    count = count + 1
    s = str( count )
    outf.write( s + "\n" )
outf.close()

print ( "Done writing to ", filename )
