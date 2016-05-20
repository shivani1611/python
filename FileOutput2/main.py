#!/usr/bin/env python3

# get sentence from the user, sort it alphabetically and output it to chosen file

def bubbleSort( arr ):
  for x in range( len( arr ) ):
    for y in range( len( arr ) - 1 ):
      if( arr[y] > ( arr[y + 1] ) ):
        tmpString = ( arr[y] )
        arr[y] = ( arr[y + 1] )
        arr[y + 1] = ( tmpString )

  return( arr )

def main( ):

  string = ( input( "Enter some words: " ) )
  while( not string ):
    string = ( input( "Enter some words: " ) )

  tmpArray = ( string.split( ' ' ) )
  bubbleSort( tmpArray )
  finalString = ( ''.join( tmpArray ) )

  string = ( input( "Enter filename to write to: " ) )
  while( not string ):
    string = ( input( "Enter filename to write to: " ) )

  try:
    fileObj = ( open( string, 'w' ) )
    fileObj.write( finalString )
    fileObj.close( )
  except IOError as e:
    print( "Unable I/O: ", string, ": ", e )
    quit( )

if( __name__ == ( "__main__" ) ):
  main( )
