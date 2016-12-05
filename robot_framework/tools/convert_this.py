class ConvertThis( object ):
    @staticmethod
    def convert_bool( obj, _raise_err = ( False ) ):
        try:
            obj = ( bool( obj ) )
        except ValueError:
            if( _raise_err == ( True ) ):
                print( "Cannot convert [\"{0}\"] to boolean".format( str( obj ) ) )
                raise
            obj = ( False )
        return( obj )

    @staticmethod
    def convert_int( obj, _raise_err = ( False ) ):
        try:
            obj = ( int( obj ) )
        except ValueError:
            if( _raise_err == ( True ) ):
                print( "Cannot convert [\"{0}\"] to integer".format( str( obj ) ) )
                raise
            obj = ( 0 )
        return( obj )

    @staticmethod
    def convert_float( obj, _raise_err = ( False ) ):
        try:
            obj = ( float( obj ) )
        except ValueError:
            if( _raise_err == ( True ) ):
                print( "Cannot convert [\"{0}\"] to floating point".format( str( obj ) ) )
                raise
            obj = ( 0.0 )
        return( obj )

    @staticmethod
    def convert_str( obj, _raise_err = ( False ) ):
        try:
            obj = ( str( obj ) )
        except ValueError:
            if( _raise_err == ( True ) ):
                print( "Cannot convert [\"{0}\"] to string".format( str( obj ) ) )
                raise
            obj = ( "" )
        return( obj )

    @staticmethod
    def convert_frozen_set( obj, _raise_err = ( True ) ):
        try:
            obj = ( frozenset( obj ) )
        except TypeError:
            obj = ( frozenset( ) )
            print( "Cannot convert [\"{0}\"] to frozen set".format( str( obj ) ) )
            raise
        return( obj )

    @staticmethod
    def convert_set( obj, _raise_err = ( True ) ):
        try:
            obj = ( set( obj ) )
        except TypeError:
            obj = ( set( ) )
            print( "Cannot convert [\"{0}\"] to set".format( str( obj ) ) )
            raise
        return( obj )

    @staticmethod
    def convert_tuple( obj, _raise_err = ( True ) ):
        try:
            obj = ( tuple( obj ) )
        except TypeError:
            obj = ( tuple( ) )
            print( "Cannot convert [\"{0}\"] to tuple".format( str( obj ) ) )
            raise
        return( obj )

    @staticmethod
    def convert_list( obj, _raise_err = ( True ) ):
        try:
            obj = ( list( obj ) )
        except TypeError:
            obj = ( list( ) )
            print( "Cannot convert [\"{0}\"] to list".format( str( obj ) ) )
            raise
        return( obj )
