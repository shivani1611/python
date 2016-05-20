#!/usr/bin/env python3

# extract the numbers from a file and calculate the sum 

from time import sleep

def main( ):
  fileName = ( input( "Enter filename to read from: " ) )
  fileLine = ( "" )
  numList = []
  sum = ( 0 )

  fileObj = ( open( fileName, 'r' ) )

  for i in fileObj:
    for x in range( 0, len( i ), 1 ):
      if( i[x].isnumeric( ) ):
        numList.append( i[x] )

  for i in numList:
    sum += ( int( i ) )  

  print( "Sum is %s" %( sum ) )

  fileObj.close( )

if( __name__ == ( "__main__" ) ):
  main( )
