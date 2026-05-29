#!/usr/bin/python3
#
# Python program to read two numbers from a file,
#   add them and print the result.
#
filename = 'numbers.txt'
inpf = open(  filename,  'r' )

s = inpf.readline()
x = int( s )
y = int( inpf.readline() )
inpf.close()

sum = x + y
print ( "The result of adding the two numbers in ", filename, " is ", sum )
