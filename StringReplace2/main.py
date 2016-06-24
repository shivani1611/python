#!/usr/bin/env python3

import sys

def main( ):

  # string 1
  a = "armond, syuzi, seda, suida"

  # string 2
  b = "syuzi"

  # remove the chosen word
  a = a.replace( b, '' )

  # remove the comma
  a = a.replace( ',', '' )

  # convert to list
  a_list = str.split( a, ' ' )

  # remove any spaced array elements
  for a in range( len( a_list ) - ( 1 ), -1, -1 ):
    if( ( not a_list[a] ) or ( a_list[a] == ' ' ) ):
      del( a_list[a] )

  # display the final array
  for a in range( 0, len( a_list ), 1 ):
    print( a_list[a] )
      

if( __name__ == ( "__main__" ) ):
  sys.exit( main( ) )
