def getSum( ):
  sum = ( 0 )
  count = ( 0 )
  num = ( 0 )

  count = ( int( input( "Enter how many numbers: " ) ) )

  for i in range( 0, count ):
    num = ( int( input( "Enter a number: " ) ) )
    sum += ( num )

  return( sum )

def main( ):
  print( "Sum:", str( getSum( ) ) )

if( __name__ == ( "__main__" ) ):
  main( )
