def calcFeet( inches ) :
  return( inches / 12 )

def main( ) :
  inches = ( int( input( "Enter inches: " ) ) )
  print( inches, "inches converted is", str( calcFeet( inches ) ), "feet" )

if( __name__ == ( "__main__" ) ) :
  main( )
