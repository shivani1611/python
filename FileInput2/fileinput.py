#!/usr/bin/env python3

def display( l ):
  for i in range( len( l ) ) :
    print( l[i], sep = ( "" ), end = ( "" ) )

def main( ):
  list = []

  fileName = ( str( input( "Enter file name to read from: " ) ) )
  file = ( open( fileName, "r" ) )

  for i in file :
    fileLine = ( i )
    list.append( fileLine )

  display( list )

if( __name__ == ( "__main__" ) ) :
  main( )
