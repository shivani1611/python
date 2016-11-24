#!/usr/bin/env python3

from sys import exit
from os  import system
import time

def main( ):
    system( 'clear' )

    isExitBuilding = ( False )

    # declare floors list
    floors = ( list( ) )

    for i in range( 1, 31, 1 ):
        floors.append( int( i ) )

    # set the current floor ( level 1 )
    current_floor = floors[29]

    while( isExitBuilding == ( False ) ):
        print( "You are currently on floor #: {0}".format( str( current_floor ) ) )

        while( True ):
            isExitBuilding = ( False )

            number = ( int( input( "\nEnter a floor # (1 to quit): " ) ) )

            if( ( number - 1 ) == ( 0 ) ):
                isExitBuilding = ( True )
                break

            if( number > ( len( floors ) ) ):
                print( "Incorrect floor, try again.." )
                time.sleep( 1 )
                continue

            if( ( ( number - 1 ) >= ( 0 ) ) and ( ( number - 1 ) <= ( 30 ) ) ):
                current_floor = ( floors[number-1] )
                break
            else:
                print( "Incorrect floor, try again.." )
                time.sleep( 1 )
                continue

if( __name__ == ( "__main__" ) ):
  exit( main( ) )
