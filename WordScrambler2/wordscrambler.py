#!/usr/bin/env python3

import random

def main( ):
  scrambled = ""
  usedElements = []

  unscrambled = input( "Enter a word to scramble: " )

  for i in range( 0, len( unscrambled ), 1 ):
    randNum = ( random.randrange( 0,  len( unscrambled ) ) )
    while( randNum in usedElements ):
      randNum = ( random.randrange( 0, len( unscrambled ) ) )
    scrambled += unscrambled[ randNum ]
    usedElements.append( randNum )

  print( scrambled )


if( __name__ == ( "__main__" ) ):
  main( )
