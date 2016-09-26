#!/usr/bin/python3

import sys

def convToString( num ):
  num_length = len( str( num ) )
  count = num_length

  conv_string = ""

  for i in range( 0, num_length, 1 ):
    conv_string += ( str( num )[i] )

    if( count > 1 ):
      conv_string += ( str( "0" * ( count - 1 ) ) )
      conv_string += ( "+" )

    count = ( count - 1 )

  return( conv_string )

def main( ):
  print( convToString( sys.argv[1] ) )

if( __name__ == ( "__main__" ) ):
  sys.exit( main( ) )
