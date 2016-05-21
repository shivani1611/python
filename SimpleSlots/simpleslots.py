#!/usr/bin/env python3

import random
from decimal import Decimal

def main( ):

  slots = [[1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7]]
  money = Decimal( 1500.00 )
  playedCount = ( 0 )
 
  while( money >= 0 ):
    playedCount += ( 1 )

    column1 = ( random.randrange( 0, len( slots[0] ), 1 ) )
    column2 = ( random.randrange( 0, len( slots[1] ), 1 ) )
    column3 = ( random.randrange( 0, len( slots[2] ), 1 ) )

    print( "Played: ", str( playedCount ), " - Money: $", str( money ), "\t[", slots[0][column1], "]\t[", slots[1][column2], "]\t[", slots[2][column3], "]", sep = ( "" ) )
    
    if( column1 == column2 == column3 ):
      money += ( Decimal( 100.00 ) )
      print( "You win!" )
    else:
      money -= ( 5 )

if( __name__ == ( "__main__" ) ):
  main( )
