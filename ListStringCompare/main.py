#!/usr/bin/env python3

import sys

def main( ):
  # list # 1
  list1 = [ "network", "cisco", "router", "osi" ]

  # string # 1
  string1 = ( "network, switch, hub, cisco, juniper, arista" )

  for a in range( len( list1 ) - ( 1 ), -1, -1 ):
    string1 = ( string1.replace( list1[a], "" ) )
    #if( list1[a] in string1 ):
      
  string1 = ( string1.replace( " ", "" ) )
  string1 = ( string1.replace( ",", " " ) )

  # convert to list2
  list2 = ( string1.split( ' ' ) )

  # remove any unnecessary space elements
  for a in range( len( list2 ) - ( 1 ), -1, -1 ):
    if( ( not list2[a] ) or ( list2[a] == ' ' ) ):
      del( list2[a] )

  # display results
  for a in range( 0, len( list2 ), 1 ):
    print( list2[a] )

if( __name__ == ( "__main__" ) ):
  sys.exit( main( ) )
