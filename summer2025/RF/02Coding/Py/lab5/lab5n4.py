#!/usr/bin/python3
#------------------------------------------
# Our function: transcribe
#  converts all Ts and ts to Us in an input
#  sequence and returns the result
#------------------------
def transcribe( seq ):
   global dnaseq
   dnaseq = seq.replace( 'T', 'U' )
   dnaseq = dnaseq.replace( 't', 'U' )
   return dnaseq
#-------------------------------------------

dnaseq = "GATCGCacgtcAGC"
rna = transcribe( dnaseq )

print ( "Starting DNA sequence is:     ", dnaseq )
print ( " and has been transcribed to  ", rna )
