def display( n ) :
  for i in range( len( n ) ) :
    print( "Name:", n[i], sep = ( " " ), end = ( "\n" ) )

def main( ) :
  names = []

  count = ( int( input( "How many items to key in: " ) ) )
  for i in range( 0, count ) :
    str_buffer = ( str( input( "Enter device name: " ) ) )
    names.append( str_buffer )

  display( names )

if( __name__ == ( "__main__" ) ) :
  main( )
