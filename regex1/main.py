from re  import search
from sys import exit

def checkRegexPattern( _pattern, _string ):
    result = ( False )

    if( search( _pattern, _string ) ):
        result = ( True )

    return( result )


def main( ):
    emailPattern = ( r"(([a-zA-Z]){1,25})(0-9)?@(([a-zA-Z]){1,23})\.([a-zA-Z]{2,5})" )

    while( True ):
        email = ( str( input( "Enter an email address: " ) ) )
        if( checkRegexPattern( emailPattern, email ) ):
            break
    print( ( ( '\n' ) + ( "Email address: " ) + ( email ) + ( '\n' ) )

if( __name__ == ( "__main__" ) ):
    exit( main( ) )
