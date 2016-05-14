#!/usr/bin/env python3

def display( l ):
  for i in range( len( l ) ):
    print( l[i] )

def bubbleSort( l ):
  for x in range( len( l ) ):
    for y in range( len( l ) - ( 1 ) ):
      if( l[y] > ( l[y + 1] ) ):
        str_buffer = ( l[y + 1] )
        l[y + 1] = ( l[y] )
        l[y] = ( str_buffer )

def main( ):
  names = []

  for i in range( 0, 3 ):
    names.append( str( input( "Enter a name: " ) ) )

  bubbleSort( names )
  display( names )

if( __name__ == ( "__main__" ) ):
  main( )
