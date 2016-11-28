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

