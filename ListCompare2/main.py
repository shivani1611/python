#!/usr/bin/env python3

import sys

def main( ):
  # full list
  list1 = [ 'armond', 'syuzi', 'seda', 'suida' ]

  # user input variable
  val = ( ' ' )
  while( val != 'x' ):
 
    # acquire user input
    val = ( input( "Enter a name to remove or \'x\' to quit: " ) )

    # check if user wants to exit
    if( val == 'x' ):
      break

    # check the occurrence for what the user entered in list1
    for a in range( len( list1 ) - ( 1 ), -1, -1 ):
      # compare val (user input variable) against list1
      if( val == ( list1[a] ) ):
        # if found, delete it
        del( list1[a] )

  # display final reslut
  for a in range( 0, len( list1 ), 1 ):
    print( list1[a] )

if( __name__ == ( "__main__" ) ):
  sys.exit( main( ) )
