#!/usr/bin/env python3

from sys import exit

def main( ):
    i = 1
    num = 1
    MAX_NUM = ( 6 )

    while( True ):
        print( str( num ) + " x " + str( i ) + " = " + str( num * i ) )

        i = ( i + ( 1 ) )

        if( i > ( MAX_NUM ) ):
          num = ( num + ( 1 ) )
          i = ( 1 )

        if( num > ( MAX_NUM ) ):
          break


if( __name__ == ( "__main__" ) ):
    exit( main( ) )
