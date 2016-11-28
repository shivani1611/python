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

