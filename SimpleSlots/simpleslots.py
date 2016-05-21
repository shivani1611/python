#!/usr/bin/env python3

import random
from decimal import Decimal

def main( ):

  slots = [["cherry", "7", "bar", "bar2", "bar3", "star", "heart"],
          ["7", "bar", "star", "heart", "cherry", "bar2", "bar3"], 
          ["heart", "star", "bar3", "bar", "cherry", "7", "bar2"]]

  money = Decimal( 1500.00 )
  playedCount = ( 0 )
 
  while( Decimal( money ) >= ( 0.0 ) ):
    playedCount += ( 1 )

    column1 = ( random.randrange( 0, len( slots[0] ), 1 ) )
    column2 = ( random.randrange( 0, len( slots[1] ), 1 ) )
    column3 = ( random.randrange( 0, len( slots[2] ), 1 ) )

    print( "Played: ", str( playedCount ), " - Money: $", str( money ), "\t[", slots[0][column1], "][", slots[1][column2], "][", slots[2][column3], "]", sep = ( "" ) )
    
    if( slots[0][column1] == slots[1][column2] == slots[2][column3] ):
      money += ( Decimal( 100.00 ) )
      print( "You win!" )
    else:
      money -= ( 5 )

if( __name__ == ( "__main__" ) ):
  main( )
