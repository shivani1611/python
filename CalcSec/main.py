#!/usr/bin/env python3

import sys

def calcSec( min ):
  return(  min * ( 60 ) )

def main( ):
  min = input ( "Enter minutes: " )
  min = ( int( min ) )

  print( "Minutes converted to seconds is: ",  calcSec( min ) )

if( __name__ == ( "__main__" ) ):
  sys.exit( main( ) )
