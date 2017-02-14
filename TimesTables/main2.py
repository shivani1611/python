#!/usr/bin/env python3

from sys import exit

def main( ):

    x = 0
    y = 0
    while( True ):
       print( str( x ) + " x " + str( y ) + " = " + str( int( x ) * int( y ) ) )
       x = x + 1
       y = y + 1


if __name__ == "__main__":
    exit( main( ) )
