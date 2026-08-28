#!/usr/bin/python3
#
# Python program showing how to use a for loop
#
listofnumbers = [ 20, 45, 50, -10 ]
size = len( listofnumbers)
sum = 0;
for count in range( size ):
    sum = sum + listofnumbers[count]

print ( " The sum of the elements of ", listofnumbers, " is ", sum )
#
# --- do the same thing as above in a different way:
#
sum = 0;
for item in listofnumbers:
    sum = sum + item
print ( " The sum of the elements of ", listofnumbers, " is ", sum )
