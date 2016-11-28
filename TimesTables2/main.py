#!/usr/bin/env python3

from sys import exit

def convert_bool( obj, _raise_err = ( False ) ):
    try:
        obj = ( bool( obj ) )
    except ValueError:
        if( _raise_err == ( True ) ):
            print( "Cannot convert [\"{0}\"] to boolean".format( str( obj ) ) )
            raise
        obj = ( False )
    return( obj )

def convert_int( obj, _raise_err = ( False ) ):
    try:
        obj = ( int( obj ) )
    except ValueError:
        if( _raise_err == ( True ) ):
            print( "Cannot convert [\"{0}\"] to integer".format( str( obj ) ) )
            raise
        obj = ( 0 )
    return( obj )

def convert_float( obj, _raise_err = ( False ) ):
    try:
        obj = ( float( obj ) )
    except ValueError:
        if( _raise_err == ( True ) ):
            print( "Cannot convert [\"{0}\"] to floating point".format( str( obj ) ) )
            raise
        obj = ( 0.0 )
    return( obj )

def convert_str( obj, _raise_err = ( False ) ):
    try:
        obj = ( str( obj ) )
    except ValueError:
        if( _raise_err == ( True ) ):
            print( "Cannot convert [\"{0}\"] to string".format( str( obj ) ) )
            raise
        obj = ( "" )
    return( obj )

def get_input( msg, _type ):
    obj = ( str( input( msg ) ).strip( ) )

    if( _type == ( int ) ):
        obj = ( convert_int( obj, _raise_err = ( False ) ) )
    elif( _type == ( float ) ):
        obj = ( convert_float( obj, _raise_err = ( False ) ) )
    elif( _type == ( str ) ):
        obj = ( convert_str( obj, _raise_err = ( False ) ) )
    elif( _type == ( bool ) ):
        obj = ( convert_bool( obj, _raise_err = ( False ) ) )
    else:
        obj = ( convert_str( obj, _raise_err = ( True ) ) )
    return( obj )

def main( ):
    counter = ( 1 )

    print( )

    num1 = ( get_input( "Enter int x: ", int ) )
    num2 = ( get_input( "Enter int y: ", int ) )

    print( )

    for x in range( 0, ( num1 + 1 ), 1 ):
        for y in range( 0, ( num2 + 1 ), 1 ):
            print( str( counter ) + ") " + str( x ) + " x " 
                 + str( y ) + " = " + str( x * y ) )
            counter += ( 1 )
        print( )
    return( 0 )

if( __name__ == ( "__main__" ) ):
    exit( main( ) )
