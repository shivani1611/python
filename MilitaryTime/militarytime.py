#!/usr/bin/env python3

import time

def main( ):
 
  h = m = s = 0
 
  while True:
    print( "0{}".format( h ) if( h >= 0 and ( h <= 9 ) ) else h
      , "0{}".format( m ) if( m >= 0 and ( m <= 9 ) ) else m
      , "0{}".format( s ) if( s >= 0 and ( s <= 9 ) ) else s
      ,  sep = ( ":" )
      , end = ( "\n" ) )

    time.sleep( .001 )
    s = s + 1

    if( s > ( 59 ) ):
      s = 0
      m = m + 1

    if( m > ( 59 ) ):
      s = 0
      m = 0
      h = h + 1

    if( h > ( 23 ) ):
      s = 0
      m = 0
      h = 0

if( __name__ == ( "__main__" ) ):
  main( )
