#!/usr/bin/python3 -W all
#
# Python program showing how to read a simple 
#  FASTA file containing a single sequence.
#
print ( "Welcome to the FASTA file reader program" )
# First, ask the user for the name of the file
filename = input(" Name of file? ")

try:
    inpf = open( filename, "r" )
except IOError as e:
    print ( "Unable to open ", filename, ". Exiting program." )
    exit()

seqinfo = inpf.readline()
print ( " Information about file: ", seqinfo )

data = inpf.readlines()  # read in the remaining data
inpf.close()
print ( " And the actual sequence data:" )
print ( data )
print ( "Done." )
