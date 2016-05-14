from sys import stdout

def calcGrade( p ) :
  letter = ( ' ' )

  if( p >= 90 and ( p <= 100 ) ) :
    letter = ( 'A' )
  elif( p >= 80 and ( p <= 89 ) ) :
    letter = ( 'B' )
  elif( p >= 70 and ( p <= 79 ) ) :
    letter = ( 'C' )
  elif( p >= 60 and ( p <= 69 ) ) :
    letter = ( 'D' )
  elif( p >= 0 and ( p <= 59 ) ) :
    letter = ( 'F' )
  else :
    letter = ( '?' )

  return( letter )

def main( ) :
  perc = ( int( input( "Enter percentage: " ) ) )
  print( "Your grade is:", calcGrade( perc ) ) 

if( __name__ == ( "__main__" ) ) :
  main( )
