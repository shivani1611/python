#!/usr/bin/env python3

import sys

def main( ):
  try:
    if( len( sys.argv ) > ( 1 ) ):
      print( sys.argv[1] )
  except IndexError as e:
    print( "Name Error: ", e )

if( __name__ == ( "__main__" ) ):
  main( )
