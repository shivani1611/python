#!/usr/bin/env python3

def main( ) :

  sum = ( 0 )

  fileName = ( str( input( "Enter filename: " ) ) )

  file = ( open( fileName, 'r' ) )

  # read the file line by line, only find the digits and add them up
  for line in file :
    for chr in range( len( line ) ) :
      if( line[chr].isdigit( ) ) :
        sum += ( int( line[chr] ) )

  file.close( )

  print( "Sum is", sum )

if( __name__ == ( "__main__" ) ) :
  main( )
