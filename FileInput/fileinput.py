#!/bin/usr/env python3

def main( ) :
  fileName = ( str( input( "Enter filename to read from: " ) ))
  file = ( open( fileName, "r" ) )
  fileContent = file.read( )
  print( fileContent )
  file.close( )

if( __name__ == ( "__main__" ) ) :
  main( )
