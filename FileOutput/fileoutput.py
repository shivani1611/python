#!/usr/bin/env python3

def main( ) :
  fileName = ( str( input( "Enter file name to write to: " ) ) )
  file = open( fileName, "w" )

  file.write( "Hello, World!" ) 

  file.close( )

if( __name__ == ( "__main__" ) ) :
  main( )
