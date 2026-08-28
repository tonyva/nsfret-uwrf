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

size = len( listofnumbers )
print ( "Done reading: there were ", size, " numbers" )
sum = 0
count = 0
while ( count < size ):
    sum = sum + listofnumbers[ count ]
    count = count + 1

average = sum/size
print ( "sum of numbers from ", infilename, " is ", sum, \
        " and the average is ", average )
