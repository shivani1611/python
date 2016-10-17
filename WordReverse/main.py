#!/usr/bin/env python3

from sys import exit

def main( ):
    word = ( str( input( "Enter a word to reverse: " ) ) )
    word = ( word[::-1] )
    print( word )
    return( 0 )

if( __name__ == ( "__main__" ) ):
    exit( main( ) )
