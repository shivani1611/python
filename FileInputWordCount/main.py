#!/bin/usr/env python3

def main( ):

  words = { } 
  bucket = [ ]

  file = ( open( input( "Enter filename: " ), 'r' ) )
  f = file.read( )
  file.close( )

  bucket = ( f.split( ) )

  # index through bucket and add words plus their frequency
  for i in range( len( bucket ) ):
    if( bucket[i] in words.keys( ) ):
      words[bucket[i]] += ( 1 )
    else:
      words[bucket[i]] = ( 1 )

  # iterate through the dictionary
  for key, value in words.items( ):
    print( key, value )

if( __name__ == ( "__main__" ) ):
  main( )
