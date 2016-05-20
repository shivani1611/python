#!/usr/bin/env python3

def main( ):

  string = ( "        python is very fun language     " )

  print( "Length:", len( string ) )
  print( "Original String:\t", string )

  string = ( string.replace( 'p', 'j' ) )
  print( "Replaced String:\t", string )

  string = ( string.upper( ) )
  print( "Upper String:\t\t", string ) 

  string = ( string.lower( ) )
  print( "Lower String:\t\t", string )

  string = ( string.swapcase( ) )
  print( "Swapcase String:\t", string )

  string = ( string.strip( ) )
  print( "Stripped String:\t", string )

  string = ( string.capitalize( ) )
  print( "Capitalized String:\t", string )

  string = ( string.title( ) )
  print( "Titled String:\t\t", string )

  string = ( string.center( 41, '*' ) )
  print( "Centered String:\t", string )

  string = ( string.join( '##' ) )
  print( "Joined String:\t\t", string )

  string = ( "--{}--".format( string ) )
  print( "Formatted String:\t", string )

  string += ( " Ever!" )
  print( "Appended String:\t", string )

if( __name__ == ( "__main__" ) ):
  main( )
