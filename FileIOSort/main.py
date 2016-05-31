def bubbleSort( l ):
  for x in range( 0, ( len( l ) ), 1 ):
    for y in range( 0, ( len( l ) - ( 1 ) ), 1 ):
      if( l[y] > ( l[y + 1] ) ):
        tmpBuffer = ( l[y + 1] )
        l[y + 1] = ( l[y] )
        l[y] = ( tmpBuffer )

def display( l ):
  for i in l:
    print( i )

def main( ):

  list = []
  content = ( "" )
  with open( "file.txt", 'r' ) as fileObj:
    content = ( fileObj.read( ) )

  list = ( content.split( ' ' ) )

  bubbleSort( list )
  display( list )


if( __name__ == ( "__main__" ) ):
  main( )
