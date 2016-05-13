def display( min, max, sum, avg ):
  print( "Min:", min )
  print( "Max:", max )
  print( "Sum:", sum )
  print( "Avg:", avg )

def main( ):
  num = count = avg = sum = min = max = 0

  count = ( int( input( "Enter count: " )  ) )

  for i in range( 0, count ): 
    num = ( int( input( "Enter number: " ) ) )

    if( num > ( max ) ):
      max = ( num )

    if( num < ( min ) ):
      min = ( num )

    sum += ( num )

  avg = ( sum / count )

  display( min, max, sum, avg )

if( __name__ == ( "__main__" ) ):
  main( )
