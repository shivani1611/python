#!/usr/bin/env python3

import sys

def main( ):
  list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  list2 = [1, 2, 3]

  # go backwards is one solution to avoid running into index problems
  # with the del function
  for i in range( len( list1 ) - ( 1 ), -1,-1 ):
    for x in range( len( list2 ) - ( 1 ), -1, -1 ):
      if( list1[i] == list2[x] ):
        del( list1[i] )

  # display the new list with the deleted values
  for a in range( 0, len( list1 ), 1 ):
    print( list1[a] )


if( __name__ == ( "__main__" ) ):
  sys.exit( main( ) )
