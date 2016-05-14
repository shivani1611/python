#!/usr/bin/python

def main( ) :

  lineCount = ( 0 )
  fileLine = ( str( input( "Enter filename to search from: " ) ) )
  searchString = ( str( input( "Enter search string: " ) ) )

  file = ( open( fileLine, "r" ) )

  for i in file :
    lineCount = lineCount + 1
    if( searchString in ( i ) ) :
      print( "Search string:", searchString, "found in line #:", lineCount )
      
  file.close( )

if( __name__ == ( "__main__" ) ) :
  main( )
