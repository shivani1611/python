#!/usr/bin/env python3

import sys

def calcYards( feet ):
  return( feet / 3 )

def main( ):
  feet = ( input( "Enter feet to calculate yards: " ) )
  print( "{0:.2f} converted into yards is {1:.2f}".format( round( float( feet ), 2 ), round( calcYards( float( feet ) ), 2 ) ) )

if( __name__ == ( "__main__" ) ):
  sys.exit( main( ) )
