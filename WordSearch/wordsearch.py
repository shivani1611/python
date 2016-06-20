#!/usr/bin/env python3

def main( ):
  names = [ "armond", "syuzi", "seda", "suida" ]

  while( True ):
    isFound = ( False )

    str_buffer = ( input( "Enter word to search or \"X\" to quit: " ) )
    str_buffer = ( str_buffer.lower( ) )

    if( str_buffer == ( "x" ) ):
      break;

    if( str_buffer != ( "x" ) ):
      for i in range( len( names ) ):
        if( names[i] == ( str_buffer ) ):
          isFound = ( True )
          break;

    if( str_buffer != ( "x" ) ):
      if( isFound == ( True ) ):
        print( "Word:", str_buffer, "found!" )
      else:
        print( "Word:", str_buffer, "not found!"  )

if( __name__ == ( "__main__" ) ):
  main( )
