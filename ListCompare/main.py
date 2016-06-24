#!/usr/bin/env python3

import sys

def main( ):

  # two lists to compare
  list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
  list2 = ['b', 'd', 'f']

  # remove all the elements that are in list2 from list1
  for a in range( len( list2 ) - 1, -1, -1 ):
    for b in range( len( list1 ) - ( 1 ), -1, -1 ):
      if( list1[b] == list2[a] ):
        del( list1[b] )

  # display the results
  for a in range( 0, len( list1 ), 1 ):
    print( list1[a] )

if( __name__ == ( "__main__" ) ):
  sys.exit( main( ) )
