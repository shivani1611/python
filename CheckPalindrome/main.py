#!/usr/bin/env python3

from sys import exit

def is_space( s ):
    is_only_space = ( True )

    for i in range( 0, len( s ), 1 ):
        if( s[i] != ( ' ' ) ):
            is_only_space = ( False )

    return( is_only_space )

def punc_strip( s ):
    s = ( s.replace( ' ', '' ) )
    s = ( s.replace( ',', '' ) )
    s = ( s.replace( '`', '' ) )
    s = ( s.replace( '~', '' ) )
    s = ( s.replace( '!', '' ) )
    s = ( s.replace( '@', '' ) )
    s = ( s.replace( '#', '' ) )
    s = ( s.replace( '$', '' ) )
    s = ( s.replace( '%', '' ) )
    s = ( s.replace( '^', '' ) )
    s = ( s.replace( '&', '' ) )
    s = ( s.replace( '*', '' ) )
    s = ( s.replace( '(', '' ) )
    s = ( s.replace( ')', '' ) )
    s = ( s.replace( '-', '' ) )
    s = ( s.replace( '_', '' ) )
    s = ( s.replace( '=', '' ) )
    s = ( s.replace( '+', '' ) )
    s = ( s.replace( '[', '' ) )
    s = ( s.replace( '{', '' ) )
    s = ( s.replace( ']', '' ) )
    s = ( s.replace( '}', '' ) )
    s = ( s.replace( '\\', '' ) )
    s = ( s.replace( '|', '' ) )
    s = ( s.replace( ';', '' ) )
    s = ( s.replace( ':', '' ) )
    s = ( s.replace( '\'', '' ) )
    s = ( s.replace( '\"', '' ) )
    s = ( s.replace( '<', '' ) )
    s = ( s.replace( '.', '' ) )
    s = ( s.replace( '>', '' ) )
    s = ( s.replace( '?', '' ) )
    s = ( s.replace( '/', '' ) )
    s = ( s.replace( '\n', '' ) )

    return( s )

def is_palindrome( s ):
    is_palindrome = ( False )
    s_len = ( len( s ) )

    if( s_len % ( 2 ) == ( 0 ) ):
        # even numbered palindrome
        temp_string = ( s[int( s_len / 2 )::1] )
    else:
        # odd numbered palindrome
        temp_string = ( s[int( s_len / 2 ) + 1::1] )

    temp_string = ( temp_string[::-1] )

    is_match = ( True )

    for i in range( 0, len( temp_string ), 1 ):
        if( s[i] != ( temp_string[i] ) ):
            is_match = ( False )

    if( is_match == ( True ) ):
        is_palindrome = ( True )

    return( is_palindrome )

def main( ):
    is_match_found = ( False )

    print( )

    while( True ):
        word = ( input( "Enter a palindrome or Q to quit: " ) )
        if( is_space( word ) == ( True ) ):
            continue
        temp_word = ( word )
        word = ( str( word ).strip( ).lower( ) )
        word = ( punc_strip( word ) )

        if( word == ( 'q' ) ):
            break

        if( len( word ) <= ( 1 ) ):
            continue

        if( is_palindrome( word ) == ( True ) ):
            is_match_found = ( True )
            print( "Palindrome Detected: [{x}]\n".format( x = str( temp_word ) ) )

    print( )

if( __name__ == ( "__main__" ) ):
    exit( main( ) )
