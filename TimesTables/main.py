#!/usr/bin/env python3

from sys import exit

def main( ):

  i = ( 0 )
  number = ( 0 )

  while( True ):
    print( str( number ) + " x "  + str( i ) + " = " + str( number * ( i ) ) )

    i = ( i + ( 1 ) )
    if( i > ( 12 ) ):
      i = ( 0 )
      number = ( number + ( 1 ) )

    if( number > ( 12 ) ):
      i = ( 0 )
      number = ( 0 )
      break


if( __name__ == ( "__main__" ) ):
  exit( main( ) )
