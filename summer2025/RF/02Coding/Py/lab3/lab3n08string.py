#!/usr/bin/python3 -W all
#
# Python program showing how to use translation tables

str1 = "Call me Ishmael."
tableinput  = 'aem'
tableoutput = 'eal'

table = str.maketrans( tableinput, tableoutput )
# Translation table is
#    a e m
#    | | |
#    v v v
#    e a l
str2 = str1.translate( table )
print ( "Started with:   ", str1, "\n translated to: ", str2 )
