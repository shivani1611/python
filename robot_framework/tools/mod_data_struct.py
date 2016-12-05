class DigitList( object ):
    def __init__( self, some_list = ( None ) ):
        self._lst = ( [] )
        if( some_list != None ):
            try:
                for i in range( 0, len( some_list ), 1 ):
                    try:
                        if( some_list[i].isdigit( ) ):
                            self._lst.append( some_list[i] )
                    except AttributeError:
                        self._lst.append( str( some_list[i] ) )
            except TypeError:
                raise TypeError( "Need to specify a digit-only list, tuple  or string" )

    def __repr__( self ):
        return( str( self._lst ) )

class AlphaList( object ):
    def __init__( self, some_list = ( None ) ):
        self._lst = ( [] )
        if( some_list != None ):
            try:
                for i in range( 0, len( some_list ), 1 ):
                    try:
                        if( some_list[i].isalpha( ) ):
                            self._lst.append( str( some_list[i] ) )
                    except AttributeError:
                        continue
            except TypeError:
                raise TypeError( "Need to specify an alpha list, tuple  or string" )

    def __repr__( self ):
        return( str( self._lst ) )

class MaxList( object ):
    def __init__( self, _max ):
        self._lst = []
        self._max = ( _max )

    def push( self, value ):
        if( not len( self._lst ) >= ( self._max ) ):
            self._lst.append( value )
         
    def __repr__( self ):            
        return( str( self._lst ) )
 
class MaxSet( object ):
    def __init__( self, _max ):
        self._set = ( set( [] ) )
        self._max = ( _max )

    def push( self, value ):
        if( not len( self._set ) >= ( self._max ) ):
            self._set.add( value )
         
    def __repr__( self ):            
        return( str( self._set ) )
